import pandas as pd

def create_risk_band(df):

    df["risk_band"] = pd.cut(
        df["probability_of_default_pd"],
        bins=[0,0.25,0.50,0.75,1],
        labels=[
            "Low Risk",
            "Medium Risk",
            "High Risk",
            "Critical Risk"
        ]
    )

    return df