import serial
import time
import csv

# Configuration
PORT = "/dev/cu.usbmodem101"
BAUD_RATE = 9600
RECORD_TIME_SECONDS = 60
OUTPUT_FILENAME = "standing2.csv"

HEADER = [
    "Timestamp(ms)",
    "AccX(g)", "AccY(g)", "AccZ(g)",
    "GyroX(dps)", "GyroY(dps)", "GyroZ(dps)"
]

print(f"Connecting to Arduino {PORT}...")

ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
time.sleep(2)

line_count = 0

try:
    with open(OUTPUT_FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        print("Waiting for CSV header...")

        # Wait until the correct header arrives
        while True:
            line = ser.readline().decode(
                "utf-8", errors="replace"
            ).strip()

            if line.split(",") == HEADER:
                writer.writerow(HEADER)
                print("Header detected. Recording started!")
                break

        start_time = time.monotonic()

        while time.monotonic() - start_time < RECORD_TIME_SECONDS:
            line = ser.readline().decode(
                "utf-8", errors="replace"
            ).strip()

            if not line:
                continue

            values = line.split(",")

            # Accept only rows with 7 numeric values
            if len(values) != 7:
                continue

            try:
                [float(value) for value in values]
            except ValueError:
                continue

            writer.writerow(values)
            line_count += 1

            if line_count % 100 == 0:
                print(f"Captured {line_count} samples...")

finally:
    ser.close()

print(f"Recording finished! Saved {line_count} samples.")
