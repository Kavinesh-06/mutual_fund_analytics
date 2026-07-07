# Fund Recommender

import pandas as pd

funds = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

recommend = (
    funds[
        funds["risk_grade"]==risk
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(recommend[
    [
        "scheme_name",
        "sharpe_ratio",
        "expense_ratio_pct"
    ]
])