# Project 1: Sensor Data Analysis Tool - Task 5: Visualize Temperature, Vibration, and Acceleration
import matplotlib.pyplot as plt
import pandas as pd

# 1. Creating a Basic Line Plot (Temperature Over Time)

# Sample sensor dataset
data = {
    'timestamp': ['10:00', '10:01', '10:02', '10:03', '10:04'],
    'temperature': [22.5, 23.0, 23.5, 24.1, 23.8],
    'vibration': [0.12, 0.15, 0.42, 0.14, 0.13]
}
df = pd.DataFrame(data)

# Create a line plot for temperature
plt.figure(figsize=(8, 4))      # Sets the width and height of the window
plt.plot(df['timestamp'], df['temperature'], marker='o', color='red', label='Temperature (°C)')

# Add labels and a title for clarity
plt.title('Industrial Motor Temperature Monitoring')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

# 2. Multi-Metrics Visualization (Subplots)

# Create a figure with 2 rows and 1 column of subplots sharing the same x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Top plot: Temperature
ax1.plot(df['timestamp'], df['temperature'], color='tab:red', marker='o')
ax1.set_ylabel('Temp (°C)')
ax1.set_title('Sensor Diagnostics Dashboard')
ax1.grid(True)

# Bottom plot: Vibration
ax2.plot(df['timestamp'], df['vibration'], color='tab:blue', marker='x')
ax2.set_ylabel('Vibration (g)')
ax2.set_xlabel('Timestamp')
ax2.grid(True)

# Adjust layout so labels don't overlap
plt.tight_layout()
plt.show()
