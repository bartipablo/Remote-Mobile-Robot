import serial
ser = serial.Serial("/dev/ttyS0", 500000)
ser.write("hi\n".encode())
ser.write("How are you?\n".encode())