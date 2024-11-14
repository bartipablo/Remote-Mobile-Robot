import machine
import time

uart1 = machine.UART(0, baudrate=500000, tx=machine.Pin(0), rx=machine.Pin(1), timeout=1000)

while True:
    message = uart1.readline()
    if message is None:
        continue
    print(message)
