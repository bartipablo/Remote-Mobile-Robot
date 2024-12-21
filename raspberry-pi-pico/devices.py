import time 


class Buzzer:
    def __init__(self, pin):
        self.pin = pin
        self.pin.value(0)

        self.enabled = False
        self.buzzer_start_time = 0

    def toggle_buzzer(self, enable):
        if enable:
            self.pin.value(1)
            self.enabled = True
            self.buzzer_start_time = time.ticks_ms()
        else:
            self.pin.value(0)
            self.enabled = False

    def is_enabled(self):
        return self.enabled
    
    
    def disable_if_time_expired(self, expiried_time):
        if self.is_enabled() and time.ticks_diff(time.ticks_ms(), self.buzzer_start_time) >= expiried_time:
            self.toggle_buzzer(False)


class VoltageMeter:
    def __init__(self, pin):
        self.pin = pin

    def read_voltage(self):
        return (self.pin.read_u16() / 98997) * 25


class Motor:
    def __init__(self, pwm_pin, motor_forward_pin, motor_backward_pin):
        self.pwm_pin = pwm_pin
        self.motor_forward_pin = motor_forward_pin
        self.motor_backward_pin = motor_backward_pin

        self.pwm_pin.duty_u16(0)
        self.motor_forward_pin.value(0)
        self.motor_backward_pin.value(0)

        self.motor_move_start_time = 0

    def move_forward(self, speed_percentage):
        speed = int(speed_percentage * 65535 / 100)
        self.pwm_pin.duty_u16(speed)
        self.motor_forward_pin.value(1)
        self.motor_backward_pin.value(0)
        self.motor_move_start_time = time.ticks_ms()


    def move_backward(self, speed_percentage):
        speed = int(speed_percentage * 65535 / 100)
        self.pwm_pin.duty_u16(speed)
        self.motor_forward_pin.value(0)
        self.motor_backward_pin.value(1)
        self.motor_move_start_time = time.ticks_ms()

    def stop(self):
        self.pwm_pin.duty_u16(0)
        self.motor_forward_pin.value(0)
        self.motor_backward_pin.value(0)

    def stop_if_time_expired(self, expiried_time):
        if time.ticks_diff(time.ticks_ms(), self.motor_move_start_time) >= expiried_time:
            self.stop()


class DriveTrain:
    def __init__(self, left_front_motor, left_back_motor, right_front_motor, right_back_motor):
        self.left_front_motor = left_front_motor
        self.left_back_motor = left_back_motor
        self.right_front_motor = right_front_motor
        self.right_back_motor = right_back_motor

    def move_forward(self, speed):
            self.left_front_motor.move_forward(speed)
            self.left_back_motor.move_forward(speed)
            self.right_front_motor.move_forward(speed)
            self.right_back_motor.move_forward(speed)

    def move_backward(self, speed):
            self.left_front_motor.move_backward(speed)
            self.left_back_motor.move_backward(speed)
            self.right_front_motor.move_backward(speed)
            self.right_back_motor.move_backward(speed)

    def move_left(self, speed):
            self.left_front_motor.move_forward(speed)
            self.left_back_motor.move_backward(speed)
            self.right_front_motor.move_backward(speed)
            self.right_back_motor.move_forward(speed)

    def move_right(self, speed):
            self.left_front_motor.move_backward(speed)
            self.left_back_motor.move_forward(speed)
            self.right_front_motor.move_forward(speed)
            self.right_back_motor.move_backward(speed)

    def move_forward_left(self, speed):
            self.left_front_motor.move_forward(speed)
            self.right_back_motor.move_forward(speed)

    def move_forward_right(self, speed):
            self.left_back_motor.move_forward(speed)
            self.right_front_motor.move_forward(speed)

    def move_backward_left(self, speed):
            self.left_back_motor.move_backward(speed)
            self.right_front_motor.move_backward(speed)

    def move_backward_right(self, speed):
            self.left_front_motor.move_backward(speed)
            self.right_back_motor.move_backward(speed)

    def rotate_right(self, speed):
            self.left_front_motor.move_forward(speed)
            self.left_back_motor.move_forward(speed)
            self.right_front_motor.move_backward(speed)
            self.right_back_motor.move_backward(speed)

    def rotate_left(self, speed):
            self.left_front_motor.move_backward(speed)
            self.left_back_motor.move_backward(speed)
            self.right_front_motor.move_forward(speed)
            self.right_back_motor.move_forward(speed)

    def stop(self):
            self.left_front_motor.stop()
            self.left_back_motor.stop()
            self.right_front_motor.stop()
            self.right_back_motor.stop()

    def stop_if_time_expired(self, expiried_time):
            self.left_front_motor.stop_if_time_expired(expiried_time)
            self.left_back_motor.stop_if_time_expired(expiried_time)
            self.right_front_motor.stop_if_time_expired(expiried_time)
            self.right_back_motor.stop_if_time_expired(expiried_time)
    