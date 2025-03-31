import serial

#Open UART serial port (TX/RX)
ser = serial.Serial("/dev/serial0",9600,timeout=1)

while True:
    if ser.in_waiting: # check if data is avaiable
        line = ser.readline().decode("utf-8").strip()
        print(f"Received: {line}")
