from flightgear_python.fg_if import TelnetConnection
import numpy as np
import get_reward
import time

"""
fgfs --fg-aircraft=~/.fgfs/aircraft-data --aircraft=f15c --telnet=socket,bi,60,localhost,5500,tcp
"""



def get_observation(telnet_conn):

    damaged = telnet_conn.get_prop('/sim/custom/damaged')
    print(" ")

# Position values_________________________________________________

    position = telnet_conn.list_props('/position/')
    position = position['properties']

    altitude_agl = float(position['/position/altitude-agl-ft'])
    altitude = float(position['/position/altitude-ft'])
    ground_elev = float(position['/position/ground-elev-ft'])
    latitude = float(position['/position/latitude-deg'])
    longitude = float(position['/position/longitude-deg'])
    sea_lev_rad = float(position['/position/sea-level-radius-ft'])



# Oriantation values___________________________________________________

    orientation = telnet_conn.list_props('/orientation/')
    orientation = orientation['properties']
    
    alph = float(orientation['/orientation/alpha-deg'])
    #beta = orientation['/orientation/beta-deg']
    heading = float(orientation['/orientation/heading-deg'])
    heading_meg = float(orientation['/orientation/heading-magnetic-deg'])
    path_deg = float(orientation['/orientation/path-deg'])

    roll = float(orientation['/orientation/roll-deg'])
    pitch = float(orientation['/orientation/pitch-deg'])
    #yaw = orientation['/orientation/yaw-deg']
    
    role_rate = float(orientation['/orientation/roll-rate-degps'])
    pitch_rate = float(orientation['/orientation/pitch-rate-degps'])
    yaw_rate = float(orientation['/orientation/yaw-rate-degps'])

    true_heading = float(orientation['/orientation/true-heading-deg'])
    side_slip = float(orientation['/orientation/side-slip-deg'])
    track_deg = float(orientation['/orientation/track-deg'])
    trach_meg_deg = float(orientation['/orientation/track-magnetic-deg'])
    #local_meg_dev = float(orientation['/orientation/local-mag-dev'])


#Velocities__________________________________________________________________________________________
    
    velocities = telnet_conn.list_props('/velocities/')
    velocities = velocities['properties']

    speed = float(velocities['/velocities/airspeed-kt'])
    down_rel_grnd = float(velocities['/velocities/down-relground-fps'])
    east_rel_grnd = float(velocities['/velocities/east-relground-fps'])
    equie = float(velocities['/velocities/equivalent-kt'])
    glideslope = float(velocities['/velocities/glideslope'])
    ground_speed = float(velocities['/velocities/groundspeed-kt'])
    north_rel_grnd = float(velocities['/velocities/north-relground-fps'])
    vel_down = float(velocities['/velocities/speed-down-fps'])
    vel_east = float(velocities['/velocities/speed-east-fps'])
    vel_north = float(velocities['/velocities/speed-north-fps'])
    ubody = float(velocities['/velocities/uBody-fps'])
    vboady = float(velocities['/velocities/vBody-fps'])
    vel_vertical = float(velocities['/velocities/vertical-speed-fps'])
    wboady = float(velocities['/velocities/wBody-fps'])
    
# Acceleration_____________________________________________________________
    accelerations  = telnet_conn.list_props('/accelerations/pilot')
    accelerations = accelerations['properties']

    x_acc = float(accelerations['/accelerations/pilot/x-accel-fps_sec'])
    y_acc = float(accelerations['/accelerations/pilot/y-accel-fps_sec'])
    z_acc = float(accelerations['/accelerations/pilot/z-accel-fps_sec'])

    wog =  telnet_conn.get_prop('/gear/gear/compression-norm')

    observe_vec = np.array([
        altitude_agl,
        altitude,
        ground_elev,
        latitude,
        longitude,
        sea_lev_rad,
        alph,
        #beta,
        heading,
        heading_meg,
        path_deg,
        roll,
        pitch,
        #yaw,                            
        role_rate,
        pitch_rate,
        yaw_rate,
        true_heading,
        side_slip,
        track_deg,
        trach_meg_deg,
        #local_meg_dev,
        speed,
        down_rel_grnd,
        east_rel_grnd,
        equie,
        glideslope,
        ground_speed,
        north_rel_grnd,
        vel_down,
        vel_east,
        vel_north,
        ubody,
        vboady,
        vel_vertical,
        wboady,
        x_acc,
        y_acc,
        z_acc,
        wog
        
    ],dtype=np.float32)
    
    observe_dict = {
        'altitude_agl' : altitude_agl,
        'altitude' : altitude,
        'ground_elev' : ground_elev,
        'latitude' :latitude,
        'longitude' :longitude,
        'sea_lev_rad' :sea_lev_rad,
        'alph' :alph,
        #'beta' :beta,
        'heading' :heading,
        'heading_meg' :heading_meg,
        'path_deg' :path_deg,
        'roll' :roll,
        'pitch' :pitch,
        #'yaw' :yaw,                            
        'role_rate' :role_rate,
        'pitch_rate' :pitch_rate,
        'yaw_rate' :yaw_rate,
        'true_heading' :true_heading,
        'side_slip' :side_slip,
        'track_deg' :track_deg,
        'trach_meg_deg' :trach_meg_deg,
        #'local_meg_dev' :local_meg_dev,
        'speed' :speed,
        'down_rel_grnd' :down_rel_grnd,
        'east_rel_grnd' :east_rel_grnd,
        'equie' :equie,
        'glideslope' :glideslope,
        'ground_speed' :ground_speed,
        'north_rel_grnd' :north_rel_grnd,
        'vel_down' :vel_down,
        'vel_east' :vel_east,
        'vel_north' :vel_north,
        'ubody' :ubody,
        'vboady' : vboady,
        'vel_vertical' : vel_vertical,
        'wboady' : wboady,
        'x_acc' : x_acc,
        'y_acc' : y_acc,
        'z_acc' : z_acc,
        'wog' : wog
    
    }

    print("speed: ", ground_speed)
    #print(f'altitude: {altitude:.10f}')
    #print(f'latitude: {latitude:.10f}')
    #print(f'longitude:{longitude:.10f}')##
    #print(observe_dict)
    return observe_vec,[altitude,damaged,longitude,latitude,wog, ground_speed]



#telnet_conn = TelnetConnection('localhost', 5500)
#telnet_conn.connect() 
#while True:
#
#    _, reward_vec = get_observation(telnet_conn)
    
#    reward = get_reward.reward(reward_vec[0],reward_vec[1],reward_vec[2],reward_vec[3],reward_vec[4])
#    print("reward: ",reward)
#    time.sleep(1)
