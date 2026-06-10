import pandas as pd

df = pd.read_csv("data/raw/credit_risk_data.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())