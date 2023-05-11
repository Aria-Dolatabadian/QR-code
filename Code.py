import pyqrcode
text = "https://github.com/Aria-Dolatabadian"

qr_code = pyqrcode.create(text)
qr_code.svg ("qr.svg",scale = 10)
