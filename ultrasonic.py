import RPi.GPIO as GPIO
import time
from datetime import datetime
GPIO.setmode(GPIO.BCM)
import buzzer
TRIG = 17 #orange
ECHO = 23 #green
SPEED_SOUND = 34300
NOTIFICATION_COOLDOWN = 0 #MINS TIL NEXT NOTIFICATION WILL BE SENT
#GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
#VARS FOR TIME
t_start = 0
t_fin = 0
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

def CheckTime():
    t_fin = datetime.now()
    time_diff = t_fin - t_start
    return round(float(time_diff.total_seconds() / 60),2)
    
if __name__ == '__main__':
    try:
        while True:
            dist = sensor()
            if dist < 10:
                print(f'Notification on cooldown FIRST : {NOTIFICATION_COOLDOWN}')

                buzzer.alarmOn()
                time.sleep(0.2)
                buzzer.alarmOff()
                time.sleep(0.2)
                if NOTIFICATION_COOLDOWN <= 0:
                    #send notification through mqtt that someone is too close
                    NOTIFICATION_COOLDOWN = 0.5
                    t_start = datetime.now()
                    print('Notification sent!')
                else:
                    
                    NOTIFICATION_COOLDOWN = NOTIFICATION_COOLDOWN - CheckTime()
                    print(f'Notification on cooldown: {NOTIFICATION_COOLDOWN}')
            else:
                buzzer.alarmOff()
            #print(f"Distance: {dist}")
            time.sleep(0.00001)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

