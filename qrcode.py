import qrcode
import image
qr=qrcode.qrcode(version=15,box_size=10,border=5)
data="https://github.com/madulika-prabusankar"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
img.save('qrgit.png')
