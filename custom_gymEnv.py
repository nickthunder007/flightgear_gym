import gymnasium as gym
import numpy as np
import observe
import telnet_control
import get_reward
import fg_env as fg_env
from stable_baselines3.common.env_checker import check_env
from flightgear_python.fg_if import TelnetConnection
import reset
from stable_baselines3 import PPO
import autostart

telnet_conn = TelnetConnection('localhost', 5500 )
telnet_conn.connect()

class CustomEnv(gym.Env):  #gym.Env

    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self,telnet_conn,eps_len=120):
        super().__init__()
        self.telnet_conn = telnet_conn
        self.counter = 0
        self.eps_len = eps_len
        print(self.eps_len)
        self.action_space = gym.spaces.Box(
            low=np.array([-1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0]),
            high=1
        )

        self.observation_space = gym.spaces.Box(
            low=np.array([0, -1000, -1000, -90, -180, 0,
                    -90, 0, 0, -360, -180, -90, -100, -100, -100, 0, -90, 0, 0,
                    0, -1000,-1000, 0, -90, 0, -1000, -1000, -1000, -1000,-1000, -1000, -1000, -1000,
                    -2000, -2000, -2000,0],dtype=np.float32), 
            
            high=np.array([100000, 100000, 30000, 90, 180, 20903000,
                    90, 360, 360, 360, 180, 90, 100, 100, 100, 360, 90, 360, 360,
                    1000, 1000, 1000, 1000, 90, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                    2000, 2000, 2000, 1],dtype=np.float32),
            #shape=(N_CHANNELS, HEIGHT, WIDTH), dtype=np.uint8
            )

    def step(self, action):
        
        #print(action)
        self.counter += 1
        print("\t counter: ",self.counter)
        telnet_control.set_control_vals(self.telnet_conn, action)
        observation,obs_rew = observe.get_observation(self.telnet_conn)
        reward = get_reward.reward(obs_rew[0], obs_rew[1], obs_rew[2], obs_rew[3], obs_rew[4],obs_rew[5])
        damaged = obs_rew[1]

        
        if(self.counter > self.eps_len or damaged==1 or get_reward.aircraft_on_track==0):
            print("greater ",self.counter, self.eps_len)
            print("damaged: ",damaged,"out of track: ",get_reward.aircraft_on_track)
            terminated = True
            #get_reward.aircraft_on_track = 1
        else:
            terminated = False

        truncated = False
        info = {'info' : "info abouit the reward"}
        
        return observation, reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        self.counter = 0
        telnet_control.set_control_vals(self.telnet_conn,np.zeros(11))
        get_reward.aircraft_on_track=1
        if seed is not None:
            np.random.seed(seed)

        reset.reset(self.telnet_conn)
        autostart.autostart(self.telnet_conn)
        observation,_ = observe.get_observation(self.telnet_conn)
        info = {"info" : 'The reset runs a function that teleports aircraft to starting position'}
        return observation,info
    
env = CustomEnv(telnet_conn)

model = PPO("MlpPolicy", env, verbose=1,n_epochs=30,n_steps=120)
model.learn(total_timesteps=30*120)
counter = 0




"""
obs,_ = env.reset()
while True:
    print("epoch: ",counter)
    print(" ")
    action, _states = model.predict(obs)
    obs, rewards, done, _, _ = env.step(action)
    print(rewards)
    counter += 1
"""