import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes
extra_codes = nav_codes - master_codes

duplicate_codes = (
    fund_master["amfi_code"]
    .duplicated()
    .sum()
)

fund_master_nulls = (
    fund_master.isnull()
    .sum()
    .sum()
)

nav_history_nulls = (
    nav_history.isnull()
    .sum()
    .sum()
)

report = f"""
DAY 1 DATA QUALITY REPORT
=========================

Fund Master Records: {len(fund_master)}
NAV History Records: {len(nav_history)}

Fund Houses: {fund_master['fund_house'].nunique()}
Categories: {fund_master['category'].nunique()}

Missing Codes: {len(missing_codes)}
Extra Codes: {len(extra_codes)}

Duplicate Codes: {duplicate_codes}

Fund Master Missing Values: {fund_master_nulls}
NAV History Missing Values: {nav_history_nulls}
"""

with open(
    "reports/day1_data_quality_report.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(report)

print("Report saved successfully.")