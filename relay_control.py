# growbotpi.py
# judascleric 2019
# prerequisites:
#   sudo apt install python3-gpiozero

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

