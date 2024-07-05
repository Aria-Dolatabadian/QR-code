import pyqrcode
text = "https://github.com/Aria-Dolatabadian"

qr_code = pyqrcode.create(text)
qr_code.svg ("qr.svg",scale = 10)



import qrcode

text = "https://www.batleylab.net/"

# Generate the QR code
qr_code = qrcode.make(text)

# Save the QR code as a JPEG file
qr_code.save("qr_code.jpg", "JPEG")
