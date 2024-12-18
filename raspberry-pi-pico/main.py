import time
import _thread
 
from machine import UART, Pin, ADC
from devices import Buzzer, VoltageMeter

# HARDWARE CONFIGURATION
LED = Pin(25, Pin.OUT)
LED.value(1)

uart1 = UART(0, baudrate=500000, tx=Pin(0), rx=Pin(1))

pin_buzzer = Pin(15, Pin.OUT)

pin_voltage_meter = ADC(Pin(26))
# HARDWARE CONFIGURATION


# SOFTWARE CONFIGURATION
buzzer = Buzzer(pin_buzzer)

voltage_meter = VoltageMeter(pin_voltage_meter)
# SOFTWARE CONFIGURATION


def message_handling(message):

    if message == b"/buzzer\n":
        buzzer.toggle_buzzer(True)

def device_handling():
    buzzer.disable_if_time_expired(600)


def transmit_read_voltage_task():
    while True:
        voltage = voltage_meter.read_voltage()
        uart1.write(str(voltage) + "\n")
        time.sleep(1)

_thread.start_new_thread(transmit_read_voltage_task, ())

# MAIN LOOP
while True:
    message = uart1.readline()

    if message is not None:
        message_handling(message)
    device_handling()
