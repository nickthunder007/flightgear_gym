from flightgear_python.fg_if import TelnetConnection
import time
import json


#with open('control2/airport_file/BIKF.json', 'r') as file:
#    reset_vec = json.load(file)

#latitude: 63.9665663100
#logitude: -22.6050099000



reset_vec = {'altitude_agl': 0, 
             'altitude': 117.58373, 
             'ground_elev': 117.58373, 
             'start_latitude': 63.96453886,   #63.96453886,    63.9911325300
             'start_longitude': -22.60544549, #-22.60544549,  -22.6054085500
             'sea_lev_rad': 20869095.24, 
             'alph': 0.0, 
             'beta': '', 
             'heading': 0.01730649904, 
             'heading_meg': 10.39021239, 
             'path_deg': 90.0, 
             'roll': 0.0, 
             'pitch': 0.0, 
             'yaw': '', 
             'role_rate': 0.000, 
             'pitch_rate': 0.0, 
             'yaw_rate': 0.0, 
             'true_heading': 0.01730649904, 
             'side_slip': 0.0, 'track_deg': 0.0, 
             'trach_meg_deg': 10.37290589, 'local_meg_dev': '', 
             'speed': 0.0, 'down_rel_grnd': 0.01445677982, 
             'east_rel_grnd': -5.234975066e-05, 'equie': 3.983598583, 
             'glideslope': 0.9490790326, 'ground_speed': 0.006137155267, 
             'north_rel_grnd': 0.01035821887, 'vel_down': -0.01445677982, 
             'vel_east': -5.234975066e-05, 'vel_north': 0.01035821887, 
             'ubody': 0.0, 'vboady': 0.0, 
             'vel_vertical': 0.0, 'wboady': 0.0,
             'x_acc': 0.0, 'y_acc': 0.0, 'z_acc': 0}

def reset(telnet_conn):
    telnet_conn.set_prop('/consumables/fuel/tank[0]/level-kg', 600)
    telnet_conn.set_prop('/consumables/fuel/tank[1]/level-kg', 700)
    telnet_conn.set_prop('/consumables/fuel/tank[2]/level-kg', 1900)
    telnet_conn.set_prop('/consumables/fuel/tank[3]/level-kg', 1500)

    for i in range(3):
        telnet_conn.set_prop('/sim/custom/damaged',0.0)
        telnet_conn.set_prop('/position/altitude-ft', reset_vec['altitude'])
        telnet_conn.set_prop('/position/latitude-deg', reset_vec['start_latitude'])
        telnet_conn.set_prop('/position/longitude-deg', reset_vec['start_longitude'])

        telnet_conn.set_prop('/position/altitude-agl-ft', reset_vec['altitude_agl'])
        telnet_conn.set_prop('/position/ground-elev-ft', reset_vec['ground_elev'])

        telnet_conn.set_prop('/position/sea-level-radius-ft', reset_vec['sea_lev_rad'])



        # Oriantation values___________________________________________________

            
        telnet_conn.set_prop('/orientation/alpha-deg', reset_vec['alph'])
        #telnet_conn.set_prop('/orientation/beta-deg', reset_vec[7])
        telnet_conn.set_prop('/orientation/heading-deg', reset_vec['heading'])
        telnet_conn.set_prop('/orientation/heading-magnetic-deg', reset_vec['heading_meg'])
        telnet_conn.set_prop('/orientation/path-deg', reset_vec['path_deg'])

        telnet_conn.set_prop('/orientation/roll-deg', reset_vec['roll'])
        telnet_conn.set_prop('/orientation/pitch-deg', reset_vec['pitch'])
        #telnet_conn.set_prop('/orientation/yaw-deg', reset_vec['yaw'])
            
        telnet_conn.set_prop('/orientation/roll-rate-degps', reset_vec['role_rate'])
        telnet_conn.set_prop('/orientation/pitch-rate-degps', reset_vec[ 'pitch_rate'])
        telnet_conn.set_prop('/orientation/yaw-rate-degps', reset_vec['yaw_rate'])

        telnet_conn.set_prop('/orientation/true-heading-deg', reset_vec['true_heading'])
        telnet_conn.set_prop('/orientation/side-slip-deg', reset_vec['side_slip'])
        telnet_conn.set_prop('/orientation/track-deg', reset_vec['track_deg'])
        telnet_conn.set_prop('/orientation/track-magnetic-deg', reset_vec['trach_meg_deg'])
        telnet_conn.set_prop('/orientation/local-mag-dev', reset_vec['local_meg_dev'])


        #Velocities__________________________________________________________________________________________

        telnet_conn.set_prop('/velocities/airspeed-kt', reset_vec['speed'])
        telnet_conn.set_prop('/velocities/down-relground-fps', reset_vec['down_rel_grnd'])
        telnet_conn.set_prop('/velocities/east-relground-fps', reset_vec['east_rel_grnd'])
        telnet_conn.set_prop('/velocities/equivalent-kt', reset_vec['equie'])
        telnet_conn.set_prop('/velocities/glideslope', reset_vec['glideslope'])
        telnet_conn.set_prop('/velocities/groundspeed-kt', reset_vec['ground_speed'])
        telnet_conn.set_prop('/velocities/north-relground-fps', reset_vec['north_rel_grnd'])
        telnet_conn.set_prop('/velocities/speed-down-fps', reset_vec['vel_down'])
        telnet_conn.set_prop('/velocities/speed-east-fps', reset_vec['vel_east'])
        telnet_conn.set_prop('/velocities/speed-north-fps', reset_vec['vel_north'])
        telnet_conn.set_prop('/velocities/uBody-fps', reset_vec['ubody'])
        telnet_conn.set_prop('/velocities/vBody-fps', reset_vec['vboady'])
        telnet_conn.set_prop('/velocities/vertical-speed-fps', reset_vec['vel_vertical'])
        telnet_conn.set_prop('/velocities/wBody-fps', reset_vec['wboady'])

        telnet_conn.set_prop('/accelerations/pilot/x-accel-fps_sec', reset_vec['x_acc'])
        telnet_conn.set_prop('/accelerations/pilot/y-accel-fps_sec', reset_vec['y_acc'])
        telnet_conn.set_prop('/accelerations/pilot/z-accel-fps_sec', reset_vec['z_acc'])
        
        time.sleep(1.5)
        telnet_conn.set_prop('/sim/custom/damaged',0)


#telnet_conn = TelnetConnection('localhost', 5500)
#telnet_conn.connect()  
#reset(telnet_conn)



"""

usr/share/games/flightgear

reset_vec = {'altitude_agl': 6.616767653, 
             'altitude': 117.58373, 
             'ground_elev': 111.2224375, 
             'latitude': 63.96453886, 
             'longitude': -22.60544549, 
             'sea_lev_rad': 20869095.24, 
             'alph': 0.4033318921, 
             'beta': '', 
             'heading': 0.01730649904, 
             'heading_meg': 10.39021239, 
             'path_deg': 90.0, 
             'roll': -0.2882466129, 
             'pitch': 0.7227226399, 
             'yaw': '', 
             'role_rate': 0.0003208909038, 
             'pitch_rate': -0.04219269507, 
             'yaw_rate': 0.0001987966727, 
             'true_heading': 0.01730649904, 
             'side_slip': -25.94930812, 'track_deg': 0.0, 
             'trach_meg_deg': 10.37290589, 'local_meg_dev': '', 
             'speed': 4.004913734, 'down_rel_grnd': 0.01445677982, 
             'east_rel_grnd': -5.234975066e-05, 'equie': 3.983598583, 
             'glideslope': 0.9490790326, 'ground_speed': 0.006137155267, 
             'north_rel_grnd': 0.01035821887, 'vel_down': -0.01445677982, 
             'vel_east': -5.234975066e-05, 'vel_north': 0.01035821887, 
             'ubody': 0.01053806146, 'vboady': 1.658365587e-05, 
             'vel_vertical': 0.01445677982, 'wboady': -0.01432630124,
             'x_acc': 0.4315988221, 'y_acc': 0.1623225419, 'z_acc': -32.2337199}


"""

"""
(myvenv) nick@Pavilion-Gaming:~/fg_projects$ python3 testing_gui.py 
{'directories': ['/sim/airport/runways'],
 'properties': {'/sim/airport/closest-airport-id': 'BIKF'}}
latitude: 63.9645627200
logitude: -22.6054707300
0
latitude: 63.9645627200
logitude: -22.6054707300
1
latitude: 63.9645627200
logitude: -22.6054707300
2
latitude: 63.9645627200
logitude: -22.6054707300
3
latitude: 63.9645635300
logitude: -22.6054707400
4
latitude: 63.9646316300
logitude: -22.6054713500
5
latitude: 63.9648199200
logitude: -22.6054729900
6
latitude: 63.9651468700
logitude: -22.6054765700
7
latitude: 63.9656271900
logitude: -22.6054835900
8
latitude: 63.9662824300
logitude: -22.6054753400
9
latitude: 63.9671401600
logitude: -22.6054303100
10
latitude: 63.9682201300
logitude: -22.6054556800
11
latitude: 63.9695480500
logitude: -22.6055587600
12
latitude: 63.9711724200
logitude: -22.6055951000
13
latitude: 63.9730727000
logitude: -22.6054193900
14
latitude: 63.9752611500
logitude: -22.6052838300
15
latitude: 63.9777703700
logitude: -22.6053254600
16
latitude: 63.9805702800
logitude: -22.6055531400
17
latitude: 63.9836487700
logitude: -22.6054979000
18
latitude: 63.9869866400
logitude: -22.6050476500
19
latitude: 63.9905816100
logitude: -22.6049081400
20
latitude: 63.9943622400
logitude: -22.6061134800
21
latitude: 63.9980614000
logitude: -22.6089815200

"""