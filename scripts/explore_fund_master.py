# scripts/explore_fund_master.py

import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("Unique Fund Houses")
print(fund_master["fund_house"].unique())

print("\nCategories")
print(fund_master["category"].value_counts())

print("\nSub Categories")
print(fund_master["sub_category"].value_counts())

print("\nRisk Categories")
print(fund_master["risk_category"].value_counts())