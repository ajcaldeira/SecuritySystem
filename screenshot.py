import cv2
import sys
sys.path.append("/home/pi/Desktop/SecuritySystem/")
import urllib.request as urllibr
import numpy as np
import process_image
from datetime import datetime
import os
import subprocess
import time
import send_email
def main():
    BASE_IMG_URL = os.getenv('BASE_IMG_URL')
    # directory = '/home/pi/Desktop/SecuritySystem/'
    stream = urllibr.urlopen('http://localhost:1654/stream.mjpg')
    WRITE_DIR = '/var/www/html/ThesisMobileApp/temp_img'
    bytes=b''
    while True:
        bytes += stream.read(1024)
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]
            bytes = bytes[b+2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            gray = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
            dateNow = datetime.now().timestamp()# time object
            IMG_NAME = str(dateNow)+ '.png' 
            cv2.imwrite(os.path.join(WRITE_DIR,IMG_NAME),i)
            process_image.ProcessImage(os.path.join(WRITE_DIR,IMG_NAME),IMG_NAME)
            full_url = str(BASE_IMG_URL) + str(IMG_NAME)
            send_email.SendEmailNotification(full_url,datetime.fromtimestamp(dateNow))
            return 1

if __name__== "__main__":
    main()
