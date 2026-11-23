# Project 1: Sensor Data Analysis Tool - Task 3: Import Sensor Datasets Using Pandas
import pandas as pd

# 1. Loading a CSV Dataset

# In a real project, load a file from a disk like this:
# df = pd.read_csv('sensor_data.csv')

# For demonstration, create a simulated Pandas DataFrame directly
data = {
    'timestamp': ['2026-06-01 10:00:00', '2026-06-01 10:01:00', '2026-06-01 10:02:00'],
    'sensor_id': ['TEMP_01', 'TEMP_01', 'TEMP_01'],
    'temperature': [22.5, 23.1, 24.8],
    'vibration': [0.12, 0.15, 0.42]
}

df = pd.DataFrame(data)

print(df)

# 2. Inspecting the Structure of the Data

# View the first 5 rows to verify the import looks correct
print(df.head())

# View data types, row counts, and memory usage
print(df.info())

# Get statistical summaries of all numerical columns
print(df.describe())
