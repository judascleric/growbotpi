#!/usr/bin/python

import Adafruit_DHT

sensor = Adafruit_DHT.AM2302
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
    t_f = temperature * 9/5.0 + 32
    print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(t_f, humidity))
else:
    print('Failed to get reading. Try again!')

