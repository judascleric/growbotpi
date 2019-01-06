import time

from relay_control import set_relay

class Humidistat():
    def __init__(self, rh_set_point, rh_range):
        self.rh_set_point = rh_set_point
        self.rh_range = rh_range
        self.last_toggle_time = time.time()
        self.max_toggle_interval = 5.0  # seconds

        self.relay_on = False
        self.relay_id = 0
        set_relay(self.relay_id, self.relay_on)

    def __del__(self):
        self.relay_on = False
        set_relay(self.relay_id, self.relay_on)

    def update(self, humidity):
        cur = time.time()
        elapsed = cur - self.last_toggle_time
        if elapsed >= self.max_toggle_interval:
            if self.relay_on and humidity > self.rh_set_point + self.rh_range:
                self.relay_on = False
                self.last_toggle_time = cur
                set_relay(self.relay_id, self.relay_on)
                print('Humidistat off')
            if not self.relay_on and humidity < self.rh_set_point:
                self.relay_on = True
                self.last_toggle_time = cur
                set_relay(self.relay_id, self.relay_on)
                print('Humidistat On')

