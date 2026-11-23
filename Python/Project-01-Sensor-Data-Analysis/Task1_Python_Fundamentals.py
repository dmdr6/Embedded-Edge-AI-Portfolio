# Project 1: Sensor Data Analysis Tool - Task 1: Python Fundamentals

# 1. Variables and Data Types

# Storing different types of sensor data
sensor_id = "TEMP_01"       # String
current_temp = 23.5         # Float
reading_count = 1500        # Integer
is_active = True            # Boolean

# 2. Control Flow (Decision Making and Repetition)

# Decision making with if/elif/else
temperature = 85.0

if temperature > 90.0:
    print("Warning: Overheating risk!")
elif temperature > 75.0:
    print("Notice: Temperature elevated.")
else:
    print("Status: Normal.")

# Repetition with a for loop (processing multiple sensor readings)
readings = [22.1, 23.0, 24.2, 21.9]
for reading in readings:
    print(f"Processing reading: {reading}°C")

# 3. Functions (Reusable Logic)

# Defining a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Calling the function
my_temp_f = celsius_to_fahrenheit(25.0)
print(my_temp_f)
