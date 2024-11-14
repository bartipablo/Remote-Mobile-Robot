class Robot:
    def __init__(self, serial):
        self.serial = serial

    def enable_buzzer(self):
        self.serial.write("/buzzer\n".encode())
        