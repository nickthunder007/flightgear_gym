import numpy as np
import json


with open('control2/airport_file/BIKF.json', 'r') as file:
    reset_vec = json.load(file)

track_x1 = reset_vec['start_latitude'] + reset_vec['rs_thresh_latitude']
track_x2 = reset_vec['start_latitude'] - reset_vec['rs_thresh_latitude']
track_x3 = reset_vec['end_latitude'] - reset_vec['re_thresh_latitude']
track_x4 = reset_vec['end_latitude'] + reset_vec['re_thresh_latitude']

track_y1 = reset_vec['start_longitude'] + reset_vec['rs_thresh_longitude']
track_y2 = reset_vec['start_longitude'] - reset_vec['rs_thresh_longitude']
track_y3 = reset_vec['end_longitude'] - reset_vec['re_thresh_longitude']
track_y4 = reset_vec['end_longitude'] + reset_vec['re_thresh_longitude']
#print(track_x1,track_y1)
#print(track_x2,track_y2)
#print(track_x3,track_y3)
#print(track_x4,track_y4)
aircraft_on_track = 1

def reward(altitude_ft,craft_damaged,long,lat,wheel_on_ground,ground_speed):
    reward = 0
    craft_x = lat
    craft_y = long

    if(ground_speed < 10):
         reward += -2
    if(wheel_on_ground > 0.0):
        print("wheels still on ground")



        if((((craft_x > track_x2) or (craft_x > track_x3)) and
           ((craft_x < track_x4) or (craft_x < track_x1))) and

            (((craft_y > track_y1) or (craft_y > track_y2)) and
            ((craft_y < track_y3) or (craft_y < track_y4)))):
                print("inside the track")
                
                reward += 2
                
        else:
            print("out of track")
            global aircraft_on_track
            aircraft_on_track = 0
            reward -= 1000
            #return reward
        

    if(craft_damaged == 1):
        print("craft_dfamfa: ",craft_damaged)
        reward -=  1000
        #return reward
    
    if(altitude_ft < 500):
        reward += -3
    
    else:
        reward += 5

    print(reward)
    return reward
    


#telnet_props = telnet_conn.list_props('/sim/custom', recurse_limit=0) #/fdm/jsbsim/gear/

"""

print("(craft_x > track_x2) ",(craft_x > track_x2))
        print("(craft_x > track_x3) ",(craft_x > track_x3))
        print("(craft_x < track_x4)", (craft_x < track_x4))
        print("(craft_x < track_x1) ",(craft_x < track_x1))
        print("(craft_y > track_y1) ",(craft_y > track_y1))
        print("(craft_y > track_y2) ",(craft_y > track_y2))
        print("(craft_y < track_y3) ",(craft_y < track_y3))
        print("(craft_y > track_y4)", (craft_y > track_y4))

"""