import streamlit as st
import pandas as pd

st.title("🤖 Model Performance")

df = pd.read_csv(
    "reports/model_comparison.csv"
)

st.dataframe(df)

st.image(
    "reports/confusion_matrix.png"
)

st.image(
    "reports/precision_recall_curve.png"
)