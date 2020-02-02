import cv2
import urllib.request as urllibr
import numpy as np
import process_image
from datetime import datetime

def NumberFaces():
    CAPTURE_COOLDOWN = False
    stream = urllibr.urlopen('http://localhost:1654/stream.mjpg')
    bytes= b''
    face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/haarcascade_frontalface_default.xml')
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
            print(faces)
            for (x,y,w,h) in faces:
                cv2.rectangle(i,(x,y),(x+w,y+h),(255,255,0),2)
                if not CAPTURE_COOLDOWN:
                    CAPTURE_COOLDOWN = True
                    IMG_NAME = str(datetime.now().time())+ '.png' # time object
                    cv2.imwrite(IMG_NAME,i)
                    process_image.ProcessImage(IMG_NAME)
                    print('image taken')
            #cv2.imshow('i', i)
            if cv2.waitKey(1) == 27:
                exit(0)   
NumberFaces()