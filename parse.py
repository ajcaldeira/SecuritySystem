import cv2
import urllib.request as urllibr
import numpy as np
import process_image
from datetime import datetime
import os
import subprocess
import time
import send_email

def CheckTime(t_start):
    t_fin = datetime.now()
    time_diff = t_fin - t_start
    return round(float(time_diff.total_seconds()),2)

def NumberFaces(US_STARTED = False): #US_STARTED to check if the Ultrasonic sensor has been started
    NOTIFICATION_COOLDOWN = 0 #MINS TIL NEXT NOTIFICATION WILL BE SENT
    NOTIF_CD_MINS = 300 # 5 mins
    FIRST_RUN = 1
    BASE_IMG_URL = os.getenv('BASE_IMG_URL')
    CAPTURE_COOLDOWN = False
    try:
        stream = urllibr.urlopen('http://localhost:1654/stream.mjpg')
    except:
        print("STREAM NOT FOUND!")
        subprocess.Popen(["python3", "simple.py", "/dev/null"], stdout=subprocess.DEVNULL)
        print("Stream Started!")
        subprocess.Popen(["python3", "ultrasonic.py"])
        US_STARTED = True
        time.sleep(5)
        NumberFaces()
    if not US_STARTED:
        os.system("pkill -9 -f ultrasonic.py")
        subprocess.Popen(["python3", "ultrasonic.py"])
        US_STARTED = True
        time.sleep(5)
    bytes= b''
    face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/haarcascade_frontalface_default.xml')
    # WRITE_DIR = '/var/www/html/ThesisMobileApp/temp_img'
    WRITE_DIR = '/home/pi/Desktop/SecuritySystem/temp_img'
    while True:
        bytes += stream.read(1024)
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]
            bytes = bytes[b+2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            gray = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)
            #print(faces)
            for (x,y,w,h) in faces:
                cv2.rectangle(i,(x,y),(x+w,y+h),(255,255,0),2)
                #first time its executing
                if(FIRST_RUN == 1):
                    t_start = datetime.now()
                if NOTIF_CD_MINS <= CheckTime(t_start) or FIRST_RUN == 1:
                    FIRST_RUN = 0 #change this so its not the first time anymore
                    NOTIFICATION_COOLDOWN = NOTIF_CD_MINS
                    t_start = datetime.now()
                    dateNow = datetime.now().timestamp()
                    IMG_NAME = str(dateNow)+ '.png' # time object
                    cv2.imwrite(os.path.join(WRITE_DIR,IMG_NAME),i)
                    process_image.ProcessImage(os.path.join(WRITE_DIR,IMG_NAME),IMG_NAME)
                    full_url = str(BASE_IMG_URL) + str(IMG_NAME)
                    send_email.SendEmailNotification(full_url,datetime.fromtimestamp(dateNow))
                    print('image taken')
                else:
                    var = CheckTime(t_start)
                    print(f"Its been {var} seconds")
                    NOTIFICATION_COOLDOWN = NOTIF_CD_MINS - CheckTime(t_start)
                    print(f'Notification on cooldown: {NOTIFICATION_COOLDOWN}')
                if not CAPTURE_COOLDOWN:
                    CAPTURE_COOLDOWN = True
                    
            #cv2.imshow('i', i)
            if cv2.waitKey(1) == 27:
                exit(0)