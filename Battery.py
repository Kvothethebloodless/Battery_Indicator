import pynotify
import pexpect
import time
import os
import subprocess
import sys
import threading
def initialize():    
    pynotify.init("Basic")
    os.chdir("/sys/class/power_supply/BAT1")
    #shell = pexpect.spawn('ls')

def charging_status_check():
    battery_status = battery_level()
    print "---------"
    time.sleep(1)
    if battery_status>battery_level():
        out = "CHARGING"            
    elif (battery_status<battery_level)and(battery_status<10):
        out = "DISCHARGING. Please connect the charger."
    else:
        out = "DISCHARGING"
    print out
    return out
        
            

def battery_level():
    cmd = "cat energy_now"
    battery_level = subprocess.check_output(cmd, shell=True)
    return float(battery_level)
def battery_full_val():
    cmd = "cat energy_full"
    battery_full_val = subprocess.check_output(cmd, shell=True)    
    return float(battery_full_val)
def battery_percent():
    battery_full = battery_full_val()
    battery_now = battery_level()
    battery_state = round((battery_now/battery_full)*100,2) 
    return battery_state
def notify(notification,alive_time,sleep_time):
    while True:
        n = pynotify.Notification(notification)
        n.show()
        time.sleep(alive_time)
        n.close()
        time.sleep(sleep_time)

    

    
    
    
##    
##    
##def battery_status_notify(delay_time):        
##    while True:      
##        battery_percent = battery_percent()
##        n = pynotify.Notification("Battery Status is: "+str(battery_state)+"%")
##        n.show()
##        time.sleep(5)
##        n.close()
##        time.sleep(delay_time)
##        if battery_state<10:
##            p = pynotify.Notification("Low Battery!!! 10% Left")
##            p.show()
##            time.sleep(1)
##            p.close()
        
            
            
##        n.show()
##        time.sleep(5)
##        n.close()
##        print delay_time
##        time.sleep(int(delay_time))
##
##
##        
    
initialize()
delay_time = float(sys.argv[1])
print delay_time

status_update = threading.Thread(target=notify(str("Battery Status is: "+str(battery_percent())+"%"),5,delay_time))
status_update.daemon = True
print "test"
charging_indicator = threading.Thread(target=notify(str(charging_status_check()),5,delay_time))
charging_indicator.daemon = True
print "second test"
#status_update.start()
charging_indicator.start()
