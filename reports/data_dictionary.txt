# Mutual Fund Analytics - Data Dictionary

# Source Datasets

| Dataset                   | Purpose                                   | Source           |
| ------------------------- | ----------------------------------------- | ---------------- |
| fund_master.csv           | Master details of all mutual fund schemes | Provided Dataset |
| nav_history.csv           | Historical Net Asset Value (NAV) data     | Provided Dataset |
| investor_transactions.csv | Investor transaction records              | Provided Dataset |
| scheme_performance.csv    | Fund returns and expense ratios           | Provided Dataset |
| aum.csv                   | Assets Under Management                   | Provided Dataset |

---

# Table: dim_fund

**Purpose**

Stores descriptive information about every mutual fund scheme.

| Column        | Data Type | Business Definition               | Source          |
| ------------- | --------- | --------------------------------- | --------------- |
| fund_id       | INTEGER   | Unique identifier for each fund   | Generated       |
| amfi_code     | INTEGER   | Official AMFI Scheme Code         | fund_master.csv |
| fund_house    | TEXT      | Asset Management Company (AMC)    | fund_master.csv |
| scheme_name   | TEXT      | Name of the mutual fund scheme    | fund_master.csv |
| category      | TEXT      | Main investment category          | fund_master.csv |
| sub_category  | TEXT      | Specific fund classification      | fund_master.csv |
| risk_category | TEXT      | Risk level assigned to the scheme | fund_master.csv |

---

# Table: dim_date

**Purpose**

Stores calendar information for time-based analysis.

| Column    | Data Type | Business Definition    | Source    |
| --------- | --------- | ---------------------- | --------- |
| date_id   | INTEGER   | Unique date identifier | Generated |
| full_date | DATE      | Calendar date          | Generated |
| year      | INTEGER   | Year                   | Generated |
| quarter   | INTEGER   | Quarter of the year    | Generated |
| month     | INTEGER   | Month number (1-12)    | Generated |
| day       | INTEGER   | Day of month           | Generated |

---

# Table: fact_nav

**Purpose**

Stores daily Net Asset Value (NAV) information.

| Column  | Data Type | Business Definition   | Source          |
| ------- | --------- | --------------------- | --------------- |
| nav_id  | INTEGER   | Unique NAV record     | Generated       |
| fund_id | INTEGER   | References dim_fund   | dim_fund        |
| date_id | INTEGER   | References dim_date   | dim_date        |
| nav     | REAL      | Daily Net Asset Value | nav_history.csv |

---

# Table: fact_transactions

**Purpose**

Stores investor purchase and redemption transactions.

| Column           | Data Type | Business Definition           | Source                    |
| ---------------- | --------- | ----------------------------- | ------------------------- |
| transaction_id   | INTEGER   | Unique transaction identifier | investor_transactions.csv |
| fund_id          | INTEGER   | References dim_fund           | dim_fund                  |
| date_id          | INTEGER   | References dim_date           | dim_date                  |
| investor_id      | INTEGER   | Investor identifier           | investor_transactions.csv |
| transaction_type | TEXT      | SIP, Lumpsum or Redemption    | investor_transactions.csv |
| amount           | REAL      | Transaction amount (₹)        | investor_transactions.csv |
| state            | TEXT      | Investor state                | investor_transactions.csv |
| kyc_status       | TEXT      | KYC verification status       | investor_transactions.csv |

---

# Table: fact_performance

**Purpose**

Stores mutual fund performance metrics.

| Column         | Data Type | Business Definition          | Source                 |
| -------------- | --------- | ---------------------------- | ---------------------- |
| performance_id | INTEGER   | Unique performance record    | Generated              |
| fund_id        | INTEGER   | References dim_fund          | dim_fund               |
| return_1y      | REAL      | One-year annual return (%)   | scheme_performance.csv |
| return_3y      | REAL      | Three-year annual return (%) | scheme_performance.csv |
| return_5y      | REAL      | Five-year annual return (%)  | scheme_performance.csv |
| expense_ratio  | REAL      | Annual expense ratio (%)     | scheme_performance.csv |

---

# Table: fact_aum

**Purpose**

Stores Assets Under Management (AUM) values.

| Column  | Data Type | Business Definition                | Source    |
| ------- | --------- | ---------------------------------- | --------- |
| aum_id  | INTEGER   | Unique AUM record                  | Generated |
| fund_id | INTEGER   | References dim_fund                | dim_fund  |
| date_id | INTEGER   | References dim_date                | dim_date  |
| aum     | REAL      | Assets Under Management (₹ Crores) | aum.csv   |

---

# Data Validation Rules

## NAV History

* Date converted to datetime format.
* Records sorted by AMFI Code and Date.
* Missing NAV values forward-filled.
* Duplicate records removed.
* NAV must be greater than zero.

## Investor Transactions

* Transaction date standardized.
* Amount must be greater than zero.
* Transaction types standardized to:

  * SIP
  * Lumpsum
  * Redemption
* KYC status validated against accepted values.

## Scheme Performance

* Return columns converted to numeric.
* Invalid numeric values converted to NULL/NaN.
* Expense ratio validated between 0.1% and 2.5%.
* Suspicious values flagged for review.

---

# Table Relationships

* dim_fund (1) → fact_nav (Many)
* dim_fund (1) → fact_transactions (Many)
* dim_fund (1) → fact_performance (Many)
* dim_fund (1) → fact_aum (Many)
* dim_date (1) → fact_nav (Many)
* dim_date (1) → fact_transactions (Many)
* dim_date (1) → fact_aum (Many)

---

# Data Sources

* Internal Mutual Fund Analytics Project Dataset
* Mutual Fund NAV API (mfapi.in) for live NAV data

---

# Notes

* All processed datasets are stored in the `data/processed/` directory.
* SQLite is used as the analytical database.
* SQLAlchemy is used to load cleaned datasets into SQLite.
* The database follows a Star Schema to optimize analytical queries.
