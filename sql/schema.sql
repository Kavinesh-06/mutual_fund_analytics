
-- Dimension Table: Fund

CREATE TABLE dim_fund (
fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER UNIQUE NOT NULL,
fund_house TEXT NOT NULL,
scheme_name TEXT NOT NULL,
category TEXT,
sub_category TEXT,
risk_category TEXT
);

-- Dimension Table: Date

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY AUTOINCREMENT,
full_date DATE UNIQUE,
year INTEGER,
quarter INTEGER,
month INTEGER,
day INTEGER
);

-- Fact Table: NAV

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
fund_id INTEGER,
date_id INTEGER,
nav REAL NOT NULL,

FOREIGN KEY (fund_id)
REFERENCES dim_fund(fund_id),

FOREIGN KEY (date_id)
REFERENCES dim_date(date_id)

);

-- Fact Table: Transactions

CREATE TABLE fact_transactions (
transaction_id INTEGER PRIMARY KEY,
fund_id INTEGER,
date_id INTEGER,
amount REAL,
transaction_type TEXT,
state TEXT,
kyc_status TEXT,
FOREIGN KEY (fund_id)
REFERENCES dim_fund(fund_id),

FOREIGN KEY (date_id)
REFERENCES dim_date(date_id)
);

-- Fact Table: Performance

CREATE TABLE fact_performance (
performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
fund_id INTEGER,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,

expense_ratio REAL,

FOREIGN KEY (fund_id)
REFERENCES dim_fund(fund_id)
);

-- Fact Table: AUM

CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
fund_id INTEGER,
date_id INTEGER,
aum REAL,
FOREIGN KEY (fund_id)
REFERENCES dim_fund(fund_id),
FOREIGN KEY (date_id)
REFERENCES dim_date(date_id)
);
