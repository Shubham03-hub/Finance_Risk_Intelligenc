import pandas as pd

df = pd.read_csv("data/raw/credit_risk_data.csv")

df = df.drop(columns=["Unnamed: 14"], errors="ignore")

df = df.drop(
    columns=[
        "Unnamed: 14"
    ],
    errors="ignore"
)

df = df.drop(
    columns=[
        "customer_id"
    ],
    errors="ignore"
)

df = pd.read_csv("data/raw/credit_risk_data.csv")

df = df.drop(columns=["Unnamed: 14"], errors="ignore")

df.to_csv(
    "data/processed/cleaned_data.csv",
    index=False
)

print("Data cleaning complete")