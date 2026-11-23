# Project 1: Sensor Data Analysis Tool - Task 7: Generate a Sensor Analysis Report
import pandas as pd
import numpy as np

# 1. Simulate the cleaned data and computed statistics
sensor_id = "MOTOR_01"
total_readings = 1000
mean_temp = 23.15
std_temp = 0.41
correlation_val = 0.9997

# 2. Design the report layout as a formatted string (f-string)
report_content = f"""
==================================================
        INDUSTRIAL SENSOR ANALYSIS REPORT
==================================================
Sensor ID: {sensor_id}
Total Data Points Processed: {total_readings}

--- STATISTICAL SUMMARY ---
- Mean Temperature: {mean_temp}°C
- Standard Deviation: {std_temp}°C
- Temperature-Vibration Correlation: {correlation_val}

--- ENGINEERING DIAGNOSIS ---
WARNING: Extremely high correlation (0.9997) detected
between temperature and vibration. This indicates potential
mechanical friction, wear, or lubrication failure.
Immediate inspection recommended.
==================================================
"""

# 3. Write the report content to a file on disk
with open("sensor_report.txt", "w") as file:
    file.write(report_content)

print("Report Successfully generated and saved as 'sensor_report.txt'!")
