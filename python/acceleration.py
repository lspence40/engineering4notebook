import Adafruit_LSM303
lsm303 = Adafruit_LSM303.LSM303()
from time import sleep

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height

padding = 2
top = padding
x = padding

font = ImageFont.load_default()

while True:
	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel
	print(accel_x, end="\t")
	print(accel_y, end="\t")
	print(accel_z)
	sleep(.5)

	image = Image.new('1', (width, height))
	draw = ImageDraw.Draw(image)

	draw.text((x, top), str(accel_x), font=font, fill=255)
	draw.text((x, top+20), str(accel_y), font=font, fill=255)
	draw.text((x, top+40), str(accel_z), font=font, fill=255)

	disp.image(image)
	disp.display()
