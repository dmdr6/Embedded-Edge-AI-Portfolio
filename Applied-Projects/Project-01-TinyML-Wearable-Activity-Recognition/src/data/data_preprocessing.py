import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Configuration

DATA_FOLDER = "."

WINDOW_SIZE = 50
OVERLAP = 25

# Sensor columns from your actual CSV files
SENSOR_COLUMNS = [
    'AccX(g)',
    'AccY(g)',
    'AccZ(g)',
    'GyroX(dps)',
    'GyroY(dps)',
    'GyroZ(dps)'
]

# Activity labels
ACTIVITY_FILES = {
    "stationary": 0,
    "stationary2": 0,
    "stationary3": 0,

    "walking": 1,
    "walking2": 1,
    "walking3": 1,

    "running": 2,
    "running2": 2,
    "running3": 2
}
