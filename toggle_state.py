import time
import os
import subprocess
def RestartNGINX():
    os.system("sudo systemctl restart nginx")


def TurnOff():
    subprocess.Popen(["python3", "/home/pi/Desktop/SecuritySystem/kill_all.py"])

def TurnOn():
    subprocess.Popen(["python3", "/home/pi/Desktop/SecuritySystem/main.py"])


def Restart():
    TurnOff()
    time.sleep(3)
    RestartNGINX()
    time.sleep(2)
    TurnOn()
    time.sleep(5)
    print("Restarted")
    
if __name__== "__main__":
  TurnOff()