# Import packages required
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "https://sakshi-weather-app.vercel.app/"

# Generate QR code
url = pyqrcode.create(s)

url.svg("weatherqr.svg", scale = 10)

url.png('weatherqr.png', scale = 12)
