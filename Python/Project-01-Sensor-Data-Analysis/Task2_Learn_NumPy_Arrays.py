# Project 1: Sensor Data Analysis Tool - Task 2: Learn NumPy Arrays

import numpy as np

# 1. Creating NumPy Arrays

# A standard Python list of vibration sensor readings
vibration_list = [0.2, 0.5, 0.1, 0.8, 0.4]

# Converting the list into a NumPy array
vibration_array = np.array(vibration_list)

print(vibration_array)
print(type(vibration_array))    # Output: <class 'numpy.ndarray'>

# 2. Vectorized Operations (No Loops Needed)

# Suppose the sensor needs a calibration multiplier of 1.05 applied to all readings
calibrated_vibration = vibration_array * 1.05

print(calibrated_vibration)     # '* 1.05' applied to every element automatically

# 3. Basic Indexing and Slicing

# Extracting specific elements
first_reading = vibration_array[0]      # 0.2 (indexes start at 0)
last_reading = vibration_array[-1]      # 0.4 (-1 refers to the last element)

# Slicing a range of readings (from index 1 up to, but not including, index 4)
subset = vibration_array[1:4]
print(subset)   # Output: [0.5, 0.1, 0.8]
