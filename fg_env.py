import os
import subprocess
import time
import random
from airports import airports
import autostart
from flightgear_python.fg_if import TelnetConnection



#check this airport KVUO, UIUN, UEVV, KDTW, UERP, UEMU, KFHR

def reset(airport_id=None):
    airport_id = airports[random.randint(0,len(airports))]
    process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 
                                'fgfs --fg-aircraft=~/.fgfs/aircraft-data --aircraft=f15c --telnet=socket,bi,60,localhost,5500,tcp --geometry=480x480 --airport=KSFO; exec bash'])# + airport_id])
    process.wait()
    #print("flight gear started")
    #time.sleep(20)
    #telnet_conn = TelnetConnection('localhost', 5500 )
    #telnet_conn.connect()
    #autostart.autostart(telnet_conn)
    return 0 #telnet_conn
