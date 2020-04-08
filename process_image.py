import base64
import sys
sys.path.append("/home/pi/Desktop/SecuritySystem/")
import writeDB

def ProcessImage(IMG_NAME):
    with open(IMG_NAME, "rb") as img_file:
        img_str = base64.b64encode(img_file.read())
        img_str = img_str[2:-1]
        writeDB.WriteImage(img_str,IMG_NAME[:-4])
    #print(img_str)