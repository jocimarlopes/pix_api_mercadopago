import qrcode
from PIL import Image
import datetime
import base64
import json

def get_name():
    date = str(datetime.datetime.now())
    b64 = base64.b64encode(date.encode()).decode()
    name = ((b64.replace('=', '')) + '.png').lower()
    print(name)
    return name

def get_qrcode(qr):
    image = qrcode.make(qr)
    name = get_name()
    image.save('./qrcode/{}'.format(name))
    im = Image.open(r"./qrcode/{}".format(name))
    im.show()

def get_credentials():
    f = open('credentials.json')
    cred = json.load(f)
    print(cred)
    return cred

""" 
    Caso o arquivo credentials.json não existir
    você precisa criar com o seguinte json:
    {
        "public_key": "SUA_PUBLIC_KEY_AQUI",
        "access_token": "SEU_ACCESS_TOKEN_AQUI"
    }
"""