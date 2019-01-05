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
    print("Setting relay {} {}".format(id, set_on))
    if set_on:
        relay_pins[id].on()
    else:
        relay_pins[id].off()


def main():
    while True:
        set_relay(0, True)
        sleep(5)
        set_relay(0, False)
        sleep(5)


if __name__ == "__main__":
    try:
        main()
    finally:
        for id in range(len(relay_pins)):
            set_relay(id, False)

