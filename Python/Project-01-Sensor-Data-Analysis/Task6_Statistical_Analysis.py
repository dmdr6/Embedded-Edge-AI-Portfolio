# Project 1: Sensor Data Analysis Tool - Task 6: Calculate Mean, Variance, Standard Deviation, and Correlation
import numpy as np
import pandas as pd

# 1. Calculating Central Tendency and Dispersion

# Sample temperature readings from a sensor
temperatures = np.array([22.5, 23.0, 22.8, 23.2, 24.5, 22.9])

# 1. Mean (Average)
mean_val = np.mean(temperatures)

# 2. Variance (Average squared distance from the mean)
variance_val = np.var(temperatures)

# 3. Standard Deviation (Square root of variance, measuring spread in original units)
std_dev_val = np.std(temperatures)

print(f"Mean: {mean_val:.2f}°C")
print(f"Variance: {variance_val:.2f}")
print(f"Standard Deviation: {std_dev_val:.2f}°C")

# 2. Calculating Correlation Between Sensors

# Create a DataFrame with two related sensor streams
data = {
    'temperature': [22.5, 23.0, 24.5, 26.0, 28.5],
    'vibration':   [0.10, 0.12, 0.18, 0.25, 0.35]
}
df = pd.DataFrame(data)

# Calculate the correlation matrix between all columns
correlation_matrix = df.corr()

print(correlation_matrix)
