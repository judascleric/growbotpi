# growbotpi.py
# judascleric 2019

import os
from time import sleep

from gpiozero import OutputDevice


relay_pins = [None, None, None, None]
relay_pins[0] = OutputDevice(17)
relay_pins[1] = OutputDevice(27)
relay_pins[2] = OutputDevice(22)
relay_pins[3] = OutputDevice(23)


def set_relay(id, set_on):
    if not set_on:  # active low
        relay_pins[id].on()
    else:
        relay_pins[id].off()


def main():
    bits = 0
    while True:
        print('bits = {:04b}'.format(bits))
        set_relay(0, True if bits & 1 else False)
        set_relay(1, True if bits & 2 else False)
        set_relay(2, True if bits & 4 else False)
        set_relay(3, True if bits & 8 else False)
        bits = (bits + 1) % 16
        sleep(2)


if __name__ == "__main__":
    try:
        main()
    finally:
        for id in range(len(relay_pins)):
            set_relay(id, False)

