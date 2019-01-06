# judascleric 2019

import time

import Adafruit_DHT as dht

class RingBuffer:
    def __init__(self, size_max):
        self.max = size_max
        self.data = []

    class __Full:
        def append(self, x):
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max
        def get(self):
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self, x):
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            self.__class__ = self.__Full

    def get(self):
        return self.data


class DHTMonitor():
    def __init__(self):
        self.sensor_data = RingBuffer(32000)
        self.min_refresh_interval = 2.0 # seconds
        self.last_reading = time.time() - self.min_refresh_interval

    def read_sensor(self):
        elapsed = time.time() - self.last_reading
        if elapsed > self.min_refresh_interval:
            humidity,temperature = dht.read_retry(dht.AM2302, 4)
            self.last_reading = time.time()
            data = {
                'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                'temperature': round(temperature * 9/5.0 + 32, 2),
                'humidity': round(humidity, 2),
            }
            self.sensor_data.append(data)

