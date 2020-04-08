from base64 import b64encode
import sys
import writeDB
import os
def ProcessImage(IMG_LOC):
    newStr = b64encode(str(IMG_LOC).encode())
    writeDB.WriteImage(newStr,IMG_LOC[:-4])
    # with open(IMG_NAME, "rb") as img_file:
    #     img_str = base64.b64encode(img_file.read())
    #     img_str = img_str[2:-1]
    #     writeDB.WriteImage(img_str,IMG_NAME[:-4])