import time
import _thread
import re

import machine
from machine import UART, Pin, ADC, PWM
from devices import Buzzer, VoltageMeter, Motor, DriveTrain

# HARDWARE CONFIGURATION
LED = Pin(25, Pin.OUT)
LED.value(1)

uart1 = UART(0, baudrate=500000, tx=Pin(0), rx=Pin(1))

pin_buzzer = Pin(15, Pin.OUT)

pin_voltage_meter = ADC(Pin(26))

left_front_motor_pwm_pin = PWM(Pin(2))
left_front_motor_pwm_pin.freq(1000)
left_front_motor_forward_pin = Pin(4, Pin.OUT)
left_front_motor_backward_pin = Pin(3, Pin.OUT)

left_back_motor_pwm_pin = PWM(Pin(7))
left_back_motor_pwm_pin.freq(1000)
left_back_motor_forward_pin = Pin(6, Pin.OUT)
left_back_motor_backward_pin = Pin(5, Pin.OUT)

right_front_motor_pwm_pin = PWM(Pin(8))
right_front_motor_pwm_pin.freq(1000)
right_front_motor_forward_pin = Pin(10, Pin.OUT)
right_front_motor_backward_pin = Pin(9, Pin.OUT)

right_back_motor_pwm_pin = PWM(Pin(13))
right_back_motor_pwm_pin.freq(1000)
right_back_motor_forward_pin = Pin(12, Pin.OUT)
right_back_motor_backward_pin = Pin(11, Pin.OUT)
# HARDWARE CONFIGURATION


# SOFTWARE CONFIGURATION
left_front_motor = Motor(left_front_motor_pwm_pin, left_front_motor_forward_pin, left_front_motor_backward_pin)
left_back_motor = Motor(left_back_motor_pwm_pin, left_back_motor_forward_pin, left_back_motor_backward_pin)
right_front_motor = Motor(right_front_motor_pwm_pin, right_front_motor_forward_pin, right_front_motor_backward_pin)
right_back_motor = Motor(right_back_motor_pwm_pin, right_back_motor_forward_pin, right_back_motor_backward_pin)

drive_train = DriveTrain(left_front_motor, left_back_motor, right_front_motor, right_back_motor)

buzzer = Buzzer(pin_buzzer)

voltage_meter = VoltageMeter(pin_voltage_meter)
# SOFTWARE CONFIGURATION


def message_handling(message):
    message_string = message.decode('utf-8')

    if message_string == "/buzzer\n":
        buzzer.toggle_buzzer(True)

    move_match = re.match("/move{(w|s|a|d|wa|wd|sa|sd|rl|rr),([1-9][0-9]?|100)}\n", message_string)
    if move_match:
        direction = move_match.group(1)
        speed = int(move_match.group(2))

        if direction == "w":
            drive_train.move_forward(speed)
        
        elif direction == "s":
            drive_train.move_backward(speed)

        elif direction == "a":
            drive_train.move_left(speed)

        elif direction == "d":
            drive_train.move_right(speed)

        elif direction == "wa":
            drive_train.move_forward_left(speed)

        elif direction == "wd":
            drive_train.move_forward_right(speed)

        elif direction == "sa":
            drive_train.move_backward_left(speed)

        elif direction == "sd":
            drive_train.move_backward_right(speed)

        elif direction == "rr":
            drive_train.rotate_right(speed)

        elif direction == "rl":
            drive_train.rotate_left(speed)

def device_handling():
    buzzer.disable_if_time_expired(600)
    drive_train.stop_if_time_expired(300)


def transmit_read_voltage_task():
    while True:
        voltage = voltage_meter.read_voltage()
        uart1.write(str(voltage) + "\n")
        time.sleep(1)

_thread.start_new_thread(transmit_read_voltage_task, ())

# MAIN LOOP
try:
    while True:
        message = uart1.readline()

        if message is not None:
            message_handling(message)
        device_handling()
except:
    drive_train.stop()
    buzzer.toggle_buzzer(False)
    for _ in range(6):  # Miganie LED przez 3 sekundy (0.5 sekundy x 6)
        LED.toggle()
        time.sleep(0.5)
    LED.value(0)    

    machine.reset()
