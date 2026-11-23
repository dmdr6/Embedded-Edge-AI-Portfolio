# Project 1: Sensor Data Analysis Tool - Task 4: Clean Missing and Incorrect Measurements
import pandas as pd
import numpy as np

# 1. Identify Missing Data

# Simulated messy dataset with missing values (NaN) and a hardware glitch (999.9)
data = {
    'timestamp': ['10:00', '10:01', '10:02', '10:03', '10:04'],
    'temperature': [22.5, np.nan, 23.1, 999.9, 23.0],
    'vibration': [0.12, 0.15, np.nan, 0.14, 0.13]
}

df = pd.DataFrame(data)

# Check how many missing values exist per column
print(df.isnull().sum())

# 2. Handling Missing Values

# Option A: Fill missing temperature values with the column mean (average)
mean_temp = df['temperature'].mean()
df['temperature'] = df['temperature'].fillna(mean_temp)

# Option B: Fill missing vibration values with a safe default baseline (0.0)
df['vibration'] = df['vibration'].fillna(0.0)

print(df)

# 3. Filtering Incorrect Measurings (Outliers)

# Define valid operational bounds for the machinery
# Temperature must be between -20°C and 100°C
valid_temp_mask = (df['temperature'] >= -20) & (df['temperature'] <= 100)

# Filter the DataFrame to keep only rows that meet the condition
df_cleaned = df[valid_temp_mask]

print(df_cleaned)   # The row with temperature 999.9 has been successfully filtered out
