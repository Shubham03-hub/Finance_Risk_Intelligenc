import streamlit as st
import pandas as pd

df = pd.read_csv(
    "data/processed/final_features.csv"
)

st.title("📊 Executive Risk Dashboard")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Total Customers",
    len(df)
)

c2.metric(
    "Average PD",
    round(
        df["probability_of_default_pd"].mean()*100,
        2
    )
)

c3.metric(
    "Average LGD",
    round(
        df["loss_given_default_lgd"].mean()*100,
        2
    )
)

c4.metric(
    "Total Expected Loss",
    round(
        df["expected_loss_el"].sum(),
        2
    )
)

st.dataframe(df.head())