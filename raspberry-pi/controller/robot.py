class Robot:
    def __init__(self, serial):
        self.serial = serial

    def enable_buzzer(self):
        self.serial.write("/buzzer\n".encode())
        
    def move_forward(self, speed):
        self.serial.write(f"/move{{w,{speed}}}\n".encode())

    def move_backward(self, speed):
        self.serial.write(f"/move{{s,{speed}}}\n".encode())

    def move_left(self, speed):
        self.serial.write(f"/move{{a,{speed}}}\n".encode())

    def move_right(self, speed):
        self.serial.write(f"/move{{d,{speed}}}\n".encode())

    def move_forward_left(self, speed):
        self.serial.write(f"/move{{wa,{speed}}}\n".encode())

    def move_forward_right(self, speed):
        self.serial.write(f"/move{{wd,{speed}}}\n".encode())

    def move_backward_left(self, speed):
        self.serial.write(f"/move{{sa,{speed}}}\n".encode())

    def move_backward_right(self, speed):
        self.serial.write(f"/move{{sd,{speed}}}\n".encode())

    def rotate_right(self, speed):
        self.serial.write(f"/move{{rr,{speed}}}\n".encode())

    def rotate_left(self, speed):
        self.serial.write(f"/move{{rl,{speed}}}\n".encode())
        