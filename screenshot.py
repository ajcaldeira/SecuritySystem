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

def main():
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
            IMG_NAME = str(datetime.now().timestamp())+ '.png' # time object
            cv2.imwrite(os.path.join(WRITE_DIR,IMG_NAME),i)
            process_image.ProcessImage(os.path.join(WRITE_DIR,IMG_NAME),IMG_NAME)
            #print(IMG_NAME[:-4])
            return 1

if __name__== "__main__":
    main()
