import serial, time
rb = serial.Serial('COM5',9600)
time.sleep(1)
rb.write(b'0')
rb.close()
