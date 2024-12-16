import qrcode
import qrcode.image.svg

LINK = 'https://www.google.com/'
img = qrcode.make(LINK, image_factory=qrcode.image.svg.SvgImage)

with open('qr.svg', 'wb') as qr:
    img.save(qr)