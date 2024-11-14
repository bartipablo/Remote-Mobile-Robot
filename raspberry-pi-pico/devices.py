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
    
    
    def disable_if_time_expired(self, time):
        if self.is_enabled() and time.ticks_diff(time.ticks_ms(), self.buzzer_start_time) >= time:
            self.toggle_buzzer(False)