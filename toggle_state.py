import time
import os
import subprocess
import sys, getopt
def RestartNGINX():
    os.system("sudo systemctl restart nginx")
    
def TurnOff():
    subprocess.Popen(["python3", "/home/pi/Desktop/SecuritySystem/kill_all.py"])

def TurnOn():
    subprocess.Popen(["python3", "/home/pi/Desktop/SecuritySystem/main.py", "/dev/null"], stdout=subprocess.DEVNULL)


def Restart():
    TurnOff()
    time.sleep(3)
    print("Turned off")
    RestartNGINX()
    time.sleep(2)
    print("Restarted Server")
    TurnOn()
    time.sleep(5)
    print("Turned On")

if __name__== "__main__":
    #r = restart
    #off = turn off
    #on = turn on
    if str(sys.argv[1]) == "r":
        Restart()
    elif str(sys.argv[1]) == "off":
        TurnOff()
    elif str(sys.argv[1]) == "on":
        TurnOn()