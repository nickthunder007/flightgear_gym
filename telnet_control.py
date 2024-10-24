from flightgear_python.fg_if import TelnetConnection
import numpy as np
from pprint import pprint

def set_control_vals(telnet_conn,control_vec):
    #control_vec = control_vec[0]
    

    telnet_conn.set_prop('/controls/flight/aileron',control_vec[0])
    telnet_conn.set_prop('/controls/flight/rudder',control_vec[1])
    telnet_conn.set_prop('/controls/flight/elevator',control_vec[2])

    telnet_conn.set_prop('/controls/flight/elevator-trim',control_vec[3])
    telnet_conn.set_prop('/controls/flight/rudder-trim',control_vec[4])
    telnet_conn.set_prop('/controls/flight/aileron-trim',control_vec[5])


    telnet_conn.set_prop('/controls/flight/flaps',control_vec[6])
    telnet_conn.set_prop('/controls/flight/spoilers',control_vec[7])
    telnet_conn.set_prop('/controls/flight/speedbrake',control_vec[8])

    telnet_conn.set_prop('/controls/flight/slats',control_vec[9])

    telnet_conn.set_prop('/controls/engines/engine/throttle',control_vec[10])
    telnet_conn.set_prop('/controls/engines/engine[1]/throttle',control_vec[10])

    return 1
