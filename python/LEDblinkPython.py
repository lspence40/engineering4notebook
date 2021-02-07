import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pin = 4
GPIO.setup(pin, GPIO.OUT)

sleep(1)

for i in range(5):
	GPIO.output(pin, 1)
	sleep(.5)
	GPIO.output(pin, 0)
	sleep(.5)

GPIO.cleanup()
