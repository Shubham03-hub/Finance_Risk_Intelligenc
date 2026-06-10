import pandas as pd

df = pd.read_csv(
    "data/processed/final_features.csv"
)

print("\nHEAD")
print(df.head(10))

print("\nCOLUMNS")
print(df.columns.tolist())

print("\nDESCRIBE")
print(df.describe())