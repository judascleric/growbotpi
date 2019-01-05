import os
from time import sleep

import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.IN)

while True:
    sleep(0.25)

