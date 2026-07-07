import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")


nav_history = pd.read_csv(
    "data/processed/nav_history_cleaned.csv"
)

nav_history.to_sql(
    "fact_nav",
    con=engine,
    if_exists="replace",
    index=False
)

transactions = pd.read_csv(
    "data/processed/investor_transaction_cleaned.csv"
)

transactions.to_sql(
    "fact_transactions",
    con=engine,
    if_exists="replace",
    index=False
)

performance = pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
)

performance.to_sql(
    "fact_performance",
    con=engine,
    if_exists="replace",
    index=False
)