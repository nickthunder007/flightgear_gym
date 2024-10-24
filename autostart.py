
def autostart(telnet_conn):


    telnet_conn.set_prop('/sim/model/f15/controls/HUD/brightness',1)
    telnet_conn.set_prop('/sim/model/f15/controls/HUD/on-off',True)
    telnet_conn.set_prop('/sim/model/f15/controls/VSD/brightness',1)
    telnet_conn.set_prop('/sim/model/f15/controls/VSD/on-off',True)
    telnet_conn.set_prop('/sim/model/f15/controls/TEWS/brightness',1)
    telnet_conn.set_prop('/sim/model/f15/controls/MPCD/brightness',1)
    telnet_conn.set_prop('/sim/model/f15/controls/MPCD/on-off',True)
    telnet_conn.set_prop('/sim/model/f15/controls/MPCD/mode',2)
    telnet_conn.set_prop('/sim/model/f15/lights/radio2-brightness',0.6)


    telnet_conn.set_prop('/sim/model/f15/controls/electrics/emerg-flt-hyd-switch',0)
    telnet_conn.set_prop('/sim/model/f15/controls/electrics/emerg-gen-guard-lever',0)
    telnet_conn.set_prop('/sim/model/f15/controls/electrics/emerg-gen-switch',1)
    telnet_conn.set_prop('/sim/model/f15/controls/electrics/l-gen-switch',1)
    telnet_conn.set_prop('/sim/model/f15/controls/electrics/master-test-switch',0)
    telnet_conn.set_prop('/sim/model/f15/controls/electrics/r-gen-switch',1)

    telnet_conn.set_prop('/controls/engines/engine[0]/cutoff',0)
    telnet_conn.set_prop('/controls/engines/engine[1]/cutoff',0)
    telnet_conn.set_prop('/engines/engine[0]/out-of-fuel',0)
    telnet_conn.set_prop('/engines/engine[1]/out-of-fuel',0)
    telnet_conn.set_prop('/engines/engine[1]/run',1)
    telnet_conn.set_prop('/engines/engine[1]/run',1)
    telnet_conn.set_prop('/sim/model/f15/controls/CAS/pitch-damper-enable',1)
    telnet_conn.set_prop('/sim/model/f15/controls/CAS/roll-damper-enable',1)
    telnet_conn.set_prop('/sim/model/f15/controls/CAS/yaw-damper-enable',1)


    telnet_conn.set_prop('/engines/engine[1]/cutoff',0)
    telnet_conn.set_prop('/engines/engine[0]/cutoff',0)

    telnet_conn.set_prop('/fdm/jsbsim/propulsion/starter_cmd',1)
    telnet_conn.set_prop('/fdm/jsbsim/propulsion/cutoff_cmd',1)
    telnet_conn.set_prop('/fdm/jsbsim/propulsion/set-running',1)
    telnet_conn.set_prop('/fdm/jsbsim/propulsion/set-running',0)

    telnet_conn.set_prop('/sim/model/f15/controls/engines/l-ramp-switch', 1)
    telnet_conn.set_prop('/sim/model/f15/controls/engines/r-ramp-switch', 1)
    telnet_conn.set_prop('/sim/model/f15/controls/fuel/dump-switch',0)
    telnet_conn.set_prop('/sim/model/f15/controls/fuel/refuel-probe-switch',0)

    telnet_conn.set_prop('/sim/model/f15/controls/engines/l-eec-switch',1)
    telnet_conn.set_prop('/sim/model/f15/controls/engines/r-eec-switch',1)
    telnet_conn.set_prop('/sim/model/f15/controls/electrics/emerg-gen-switch',1)
    telnet_conn.set_prop('/sim/model/f15/controls/engs/l-eng-master-guard',0)
    telnet_conn.set_prop('/sim/model/f15/controls/engs/r-eng-master-guard',0)

    return 1


"""
print(telnet_conn.get_prop('/sim/model/f15/controls/HUD/brightness'))
print(telnet_conn.get_prop('/sim/model/f15/controls/HUD/on-off'))
print(telnet_conn.get_prop('/sim/model/f15/controls/VSD/brightness'))
print(telnet_conn.get_prop('/sim/model/f15/controls/VSD/on-off'))
print(telnet_conn.get_prop('/sim/model/f15/controls/TEWS/brightness'))
print(telnet_conn.get_prop('/sim/model/f15/controls/MPCD/brightness'))
print(telnet_conn.get_prop('/sim/model/f15/controls/MPCD/on-off'))
print(telnet_conn.get_prop('/sim/model/f15/controls/MPCD/mode'))
print(telnet_conn.get_prop('/sim/model/f15/lights/radio2-brightness'))


print(telnet_conn.get_prop('/sim/model/f15/controls/electrics/emerg-flt-hyd-switch'))
print(telnet_conn.get_prop('/sim/model/f15/controls/electrics/emerg-gen-guard-lever'))
print(telnet_conn.get_prop('/sim/model/f15/controls/electrics/emerg-gen-switch'))
print(telnet_conn.get_prop('/sim/model/f15/controls/electrics/l-gen-switch'))
print(telnet_conn.get_prop('/sim/model/f15/controls/electrics/master-test-switch'))
print(telnet_conn.get_prop('/sim/model/f15/controls/electrics/r-gen-switch'))

print(telnet_conn.get_prop('/controls/engines/engine[0]/cutoff'))
print(telnet_conn.get_prop('/controls/engines/engine[1]/cutoff'))
print(telnet_conn.get_prop('/engines/engine[0]/out-of-fuel'))
print(telnet_conn.get_prop('/engines/engine[1]/out-of-fuel'))
print(telnet_conn.get_prop('/engines/engine[1]/run'))
print(telnet_conn.get_prop('/engines/engine[1]/run'))
print(telnet_conn.get_prop('/sim/model/f15/controls/CAS/pitch-damper-enable'))
print(telnet_conn.get_prop('/sim/model/f15/controls/CAS/roll-damper-enable'))
print(telnet_conn.get_prop('/sim/model/f15/controls/CAS/yaw-damper-enable'))


print(telnet_conn.get_prop('/engines/engine[1]/cutoff'))
print(telnet_conn.get_prop('/engines/engine[0]/cutoff'))

print(telnet_conn.get_prop('/fdm/jsbsim/propulsion/starter_cmd'))
print(telnet_conn.get_prop('/fdm/jsbsim/propulsion/cutoff_cmd'))
#print(telnet_conn.get_prop('/fdm/jsbsim/propulsion/set-running'))
#print(telnet_conn.get_prop('/fdm/jsbsim/propulsion/set-running'))

print(telnet_conn.get_prop('/sim/model/f15/controls/engines/l-ramp-switch'))
print(telnet_conn.get_prop('/sim/model/f15/controls/engines/r-ramp-switch'))
print(telnet_conn.get_prop('/sim/model/f15/controls/fuel/dump-switch'))
print(telnet_conn.get_prop('/sim/model/f15/controls/fuel/refuel-probe-switch'))

print(telnet_conn.get_prop('/sim/model/f15/controls/engines/l-eec-switch'))
print(telnet_conn.get_prop('/sim/model/f15/controls/engines/r-eec-switch'))
print(telnet_conn.get_prop('/sim/model/f15/controls/electrics/emerg-gen-switch'))
print(telnet_conn.get_prop('/sim/model/f15/controls/engs/l-eng-master-guard'))
print(telnet_conn.get_prop('/sim/model/f15/controls/engs/r-eng-master-guard'))
"""