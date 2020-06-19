import base64

def base2img(base64):
    imgdata = base64.b64decode(sys.argv[1])
    with open('CURRENT_IMAGE.png', 'wb') as f:
        f.write(imgdata)

