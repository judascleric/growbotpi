# thingsboard.py
# judascleric 2019
# prerequisites:
#   thingsboard server, with configured device + access token
#   sudo pip3 install paho-mqtt

import json
import paho.mqtt.client as mqtt

class ThingsBoardClient():
    def __init__(self):
        thingsboard_host = 'jester'
        with open('/home/pi/thingsboard/token.txt') as f:
            access_token = f.read().strip()
        self.client = mqtt.Client()
        self.client.username_pw_set(access_token)
        self.client.connect(thingsboard_host, 1883, 60)
        self.client.loop_start()

    def __del__(self):
        self.client.loop_stop()
        self.client.disconnect()
        
    def publish(self, data):
        self.client.publish('v1/devices/me/telemetry', json.dumps(data), 1)

