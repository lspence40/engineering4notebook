import Adafruit_LSM303
lsm303 = Adafruit_LSM303.LSM303()
from time import sleep
import RPi.GPIO as GPIO

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from math import sqrt

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

GPIO.setmode(GPIO.BCM)
pin = 12
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height

data = [32 for i in range(30)]

font = ImageFont.load_default()

done = False
while not done:
	image = Image.new('1', (width, height))
	draw = ImageDraw.Draw(image)

	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel
	accel_total = sqrt(accel_x*accel_x + accel_y*accel_y + accel_z*accel_z)

	temp = data[len(data)-1]
	for i in range(len(data)-1, 0, -1):
		data[i] = data[i-1]

	data[0] = 38-((accel_total-981)//10)

	for i in range(len(data)-1):
		draw.line((i*10+20, data[i], (i*10)+30, data[i+1]), fill=255)
	draw.text((5,27), str(int(data[0])-32), font=font, fill=255)

	if GPIO.input(pin):
		done = True
		image = Image.new('1', (width, height))

	disp.image(image)
	disp.display()

GPIO.cleanup()
