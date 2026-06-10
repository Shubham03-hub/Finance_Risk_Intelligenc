import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_data.csv"
)

df = df.drop(
    columns=[
        "customer_id",
        "Unnamed: 14"
    ],
    errors="ignore"
)

df.to_csv(
    "data/processed/final_features.csv",
    index=False
)