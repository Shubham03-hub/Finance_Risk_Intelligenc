# File: src/project_audit_full.py

import pandas as pd
import os
from datetime import datetime

def load_dataset(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path)

def basic_audit(df: pd.DataFrame):
    report = {}

    report["shape"] = df.shape
    report["columns"] = list(df.columns)
    report["missing_values"] = df.isnull().sum().to_dict()
    report["duplicate_rows"] = int(df.duplicated().sum())
    report["dtypes"] = df.dtypes.astype(str).to_dict()

    numeric_cols = df.select_dtypes(include=["number"]).columns
    report["numeric_summary"] = df[numeric_cols].describe().to_dict()

    return report

def save_report(report, output_path="audit_report.json"):
    import json
    with open(output_path, "w") as f:
        json.dump(report, f, indent=4, default=str)

def run_audit():
    data_path = "data/raw/credit_risk_data.csv"

    print("Loading dataset...")
    df = load_dataset(data_path)

    print("Running audit...")
    report = basic_audit(df)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"audit_report_{timestamp}.json"

    save_report(report, output_file)

    print(f"Audit complete. Report saved to {output_file}")

if __name__ == "__main__":
    run_audit()