import pandas as pd
df = pd.read_csv("data/raw/08_investor_transactions.csv")

mapping = {
    "sip":"SIP",
    "Sip":"SIP",
    "SIP":"SIP",

    "lumpsum":"Lumpsum",
    "Lumpsum":"Lumpsum",

    "redemption":"Redemption",
    "redeem":"Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
    .replace(mapping)
)
df = df[df["amount_inr"] > 0]
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]
invalid = df[
    ~df["kyc_status"]
    .isin(valid_kyc)
]
df.to_csv(
    "data/processed/investor_transaction_cleaned.csv",
    index=False
)
print(df.shape)