import json
import time
import paho.mqtt.client as mqtt
import Adafruit_DHT as dht

def main():
    thingsboard_host = 'jester'
    with open('/home/pi/thingsboard/token.txt') as f:
        access_token = f.read().strip()
    sensor_data = {'temperature': 0, 'humidity': 0}
    next_reading = time.time() 

    client = mqtt.Client()
    client.username_pw_set(access_token)
    client.connect(thingsboard_host, 1883, 60)

    client.loop_start()

    try:
        while True:
            humidity,temperature = dht.read_retry(dht.AM2302, 4)
            humidity = round(humidity, 2)
            t_f = round(temperature * 9/5.0 + 32, 2)
            print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(t_f, humidity))
            sensor_data['temperature'] = t_f
            sensor_data['humidity'] = humidity
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
            time.sleep(2)
    except KeyboardInterrupt:
        pass

    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
  main()

