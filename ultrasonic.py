import RPi.GPIO as GPIO
import time
from datetime import datetime
GPIO.setmode(GPIO.BCM)
import buzzer
TRIG = 17 #orange
ECHO = 23 #green
SPEED_SOUND = 34300
NOTIFICATION_COOLDOWN = 0 #MINS TIL NEXT NOTIFICATION WILL BE SENT
NOTIF_CD_MINS = 5
#GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
#VARS FOR TIME
t_start = 0
t_fin = 0
FIRST_RUN = 1
def sensor():
    GPIO.output(TRIG,False)
    #initialise
    pulse_start = 0
    pulse_end = 0
    #time for it to start
    time.sleep(0.1)

    GPIO.output(TRIG,True)
    time.sleep(0.0000001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start

    distance = (pulse_duration * SPEED_SOUND) /2
    distance = round(distance,2)
    return distance

def CheckTime(t_start):
    t_fin = datetime.now()
    time_diff = t_fin - t_start
    return round(float(time_diff.total_seconds() / 60),2)
    
if __name__ == '__main__':
    try:
        while True:
            dist = sensor()
            if dist < 10:
                buzzer.alarmOn()
                time.sleep(0.2)
                buzzer.alarmOff()
                time.sleep(0.2)
                #first time its executing
                if(FIRST_RUN == 1):
                    t_start = datetime.now()  
                if NOTIF_CD_MINS <= CheckTime(t_start) or FIRST_RUN == 1:
                    FIRST_RUN = 0 #change this so it snot the first time anymore
                    NOTIFICATION_COOLDOWN = NOTIF_CD_MINS
                    t_start = datetime.now()
                    print('Notification sent!')
                else:
                    var = CheckTime(t_start)
                    print(f"Its been {var} seconds")
                    NOTIFICATION_COOLDOWN = NOTIF_CD_MINS - CheckTime(t_start)
                    print(f'Notification on cooldown: {NOTIFICATION_COOLDOWN}')
            else:
                buzzer.alarmOff()
            #print(f"Distance: {dist}")
            time.sleep(0.00001)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

