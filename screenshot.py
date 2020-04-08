import cv2
import urllib.request as urllibr
import numpy as np
import process_image
from datetime import datetime
import os
import subprocess
import time

def main():
    stream = urllibr.urlopen('http://localhost:1654/stream.mjpg')
    bytes=b''
    while True:
        bytes += stream.read(1024)
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        print(a)
        print(b)
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]
            bytes = bytes[b+2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            gray = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
            IMG_NAME = str(datetime.now().time())+ '.png' # time object
            cv2.imwrite(IMG_NAME,i)
            process_image.ProcessImage(IMG_NAME)
            print('image taken')
            return 1

if __name__== "__main__":
    main()
