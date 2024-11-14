import time

from machine import UART, Pin
from devices import Buzzer

# HARDWARE CONFIGURATION
uart1 = UART(0, baudrate=500000, tx=Pin(0), rx=Pin(1))

pin_buzzer = Pin(15, Pin.OUT)
# HARDWARE CONFIGURATION


# SOFTWARE CONFIGURATION
buzzer = Buzzer(pin_buzzer)
# SOFTWARE CONFIGURATION


def message_handling(message):

    if message == b"/buzzer\n":
        buzzer.toggle_buzzer(True)

def device_handling():
    buzzer.disable_if_time_expired(600)


while True:
    message = uart1.readline()

    if message is not None:
        message_handling(message)
    device_handling()
