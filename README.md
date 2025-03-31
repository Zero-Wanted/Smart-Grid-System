# Smart-Grid-System
# Raspberry Pi & Arduino Sensor Logger

This project logs sensor data from an Arduino, sends it to a Raspberry Pi via RX/TX, and visualizes it with Python.

## Features
- Reads sensor values from Arduino using analog pins
- Sends data to Raspberry Pi via serial communication
- Logs sensor data into a CSV file
- Visualizes real-time data using matplotlib

## Setup
1. **Arduino**: Upload the provided Arduino sketch.
2. **Raspberry Pi**:
   - Install dependencies: `pip install pandas matplotlib pyserial`
   - Run `data_logger.py` to log sensor data.
   - Run `visualize.py` to display a graph.

## Project Files
- `main.py` – Main script to manage the process.
- `data_logger.py` – Logs sensor data into a CSV file.
- `visualize.py` – Plots sensor data from the CSV file.

## Requirements
- Arduino (e.g., Arduino Mega)
- Raspberry Pi
- Python 3.x
- Libraries: pandas, matplotlib, pyserial
