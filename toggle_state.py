import time
import os

def RestartNGINX():
    os.system("sudo systemctl restart nginx")


def TurnOff():
    os.system("python3 /home/pi/Desktop/SecuritySystem/kill_all.py")

def TurnOn():
    os.system("python3 /home/pi/Desktop/SecuritySystem/main.py")
    
def Restart():
    TurnOff()
    time.sleep(3)
    TurnOn()
    time.sleep(5)
    print("Restarted")
