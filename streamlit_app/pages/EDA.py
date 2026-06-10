import streamlit as st
import pandas as pd
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "final_features.csv"
)

df = pd.read_csv(DATA_PATH)
import streamlit as st

st.title("📈 Exploratory Data Analysis")

st.image(
    "reports/figures/correlation_heatmap.png"
)

st.image(
    "reports/figures/pd_distribution.png"
)

st.image(
    "reports/figures/income_vs_pd.png"
)

st.image(
    "reports/figures/loan_vs_expected_loss.png"
)

st.image(
    "reports/figures/boxplots.png"
)