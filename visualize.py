import pandas as pd
import matplotlib.pyplot as plt

data_file = 'sensor_data.csv'

data = pd.read_csv(data_file, header=0)

data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')

data['Sensor1'] = pd.to_numeric(data['Sensor1'], errors='coerce')  # Handle any invalid data
data['Sensor2'] = pd.to_numeric(data['Sensor2'], errors='coerce')  # Handle any invalid data

plt.figure(figsize=(10, 6))

plt.plot(data['Timestamp'], data['Sensor1'], label="Sensor 1", color='b')
plt.plot(data['Timestamp'], data['Sensor2'], label="Sensor 2", color='r')

plt.xlabel("Timestamp")
plt.ylabel("Sensor Value")
plt.title("Sensor Data Over Time")
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()
