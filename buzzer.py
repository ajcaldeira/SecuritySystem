from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(24)
def alarmOn():
    buzzer.on()
    
def alarmOff():
    buzzer.off()
        