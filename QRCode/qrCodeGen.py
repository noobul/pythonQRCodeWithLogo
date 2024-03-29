import pyqrcode
from PIL import Image

url = pyqrcode.QRCode('https://www.facebook.com/Annasurbangarden/', error = 'H')
url.png('test.png',scale=8)
im = Image.open('test.png')
im = im.convert("RGBA")
logo = Image.open('logo.png')
box = (140,140,230,230)
im.crop(box)
region = logo
region = region.resize((box[3] - box[1], box[3] - box[1]))
im.paste(region,box)
im.show()
im = im.save('final.png')