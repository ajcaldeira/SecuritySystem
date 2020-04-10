from base64 import b64encode
import sys
import writeDB
import os
def ProcessImage(IMG_LOC,IMG_NAME):
    newStr = b64encode(str(IMG_LOC).encode())
    writeDB.WriteImage(newStr,IMG_NAME[:-4])