import pandas as pd
import os

files = [
    "stationary.csv",
    "stationary2.csv",
    "stationary3.csv",
    "walking.csv",
    "walking2.csv",
    "walking3.csv",
    "running.csv",
    "running2.csv",
    "running3.csv"
]

for filename in files:

    print("\n" + "=" * 50)
    print("FILE:", filename)
    print("=" * 50)

    if not os.path.exists(filename):
        print("File not found!")
        continue

    df = pd.read_csv(filename)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nData types:")
    print(df.dtypes)

    print("\nDataset dimensions")
    print(df.shape)
