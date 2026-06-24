import pandas as pd
from pathlib import Path

raw_path = Path("./data/raw")

csv_files = raw_path.glob("*.csv")

for file in csv_files:

    print("="*50)
    print(f"Dataset : {file.name}")
    print("="*50)

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")