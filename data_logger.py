import serial
import csv
from datetime import datetime

SERIAL_PORT = "/dev/ttyS0"
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

csv_filename = "sensor_data.csv"

with open(csv_filename, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Sensor1", "Sensor2"])

    print("Logging data... Press Ctrl+C to stop.")

    try:
        while True:
            data = ser.readline().decode("utf-8").strip()
            if data:
                print(f"Received: {data}")
                sensor_values = data.split(",")

                if len(sensor_values) == 2:
                    sensor1 = sensor_values[0].split(":")[1].strip()
                    sensor2 = sensor_values[1].split(":")[1].strip()

                    writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), sensor1, sensor2])
    except KeyboardInterrupt:
        print("\nLogging stopped.")
        ser.close()
