import base64
import sys
import writeDB
import os
def ProcessImage(IMG_NAME):
    newStr = base64.base64encode(os.path.join(WRITE_DIR,IMG_NAME))
    writeDB.WriteImage(newStr,IMG_NAME[:-4])
    # with open(IMG_NAME, "rb") as img_file:
    #     img_str = base64.b64encode(img_file.read())
    #     img_str = img_str[2:-1]
    #     writeDB.WriteImage(img_str,IMG_NAME[:-4])