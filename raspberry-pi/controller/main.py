import serial
ser = serial.Serial("/dev/ttyS0", 500000)
ser.write("/buzzer\n".encode())
