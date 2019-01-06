# growbotpi.py
# judascleric 2019

import os
from time import sleep

from monitor_dht import DHTMonitor
from humidistat import Humidistat
from thingsboard import ThingsBoardClient

def main():
    monitor = DHTMonitor()
    humidistat = Humidistat(55, 5)
    thingsboard = ThingsBoardClient()

    update_interval = 5.0

    try:
        while True:
            monitor.read_sensor()
            sensor_data = monitor.sensor_data.get()
            if len(sensor_data) != 0:
                cur_data = sensor_data[-1]
                print('Read DHT: {}'.format(cur_data))
                humidity = cur_data['humidity']
                humidistat.update(humidity)
                thingsboard.publish(cur_data)
            else:
                print('No Temp/Humidity data')

            sleep(update_interval)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
  main()

