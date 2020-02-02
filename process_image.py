import base64
def ProcessImage(IMG_NAME):
    with open(IMG_NAME, "rb") as img_file:
        img_str = base64.b64encode(img_file.read())
    print(img_str)