import streamlit as st
import pandas as pd
import plotly.express as px
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
import pandas as pd
import plotly.express as px

st.title("Portfolio Risk Analytics")

df = pd.read_csv(
    "data/processed/final_features.csv"
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    len(df)
)

col2.metric(
    "Average PD",
    round(
        df["probability_of_default_pd"].mean(),
        3
    )
)

col3.metric(
    "Average LGD",
    round(
        df["loss_given_default_lgd"].mean(),
        3
    )
)

col4.metric(
    "Total Expected Loss",
    f"${df['expected_loss_el'].sum():,.0f}"
)

st.divider()

df["risk_band"] = pd.cut(
    df["probability_of_default_pd"],
    bins=[0,0.25,0.50,0.75,1],
    labels=[
        "Low",
        "Medium",
        "High",
        "Critical"
    ]
)

fig = px.histogram(
    df,
    x="risk_band",
    title="Portfolio Risk Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig2 = px.scatter(
    df,
    x="financial_stress_score",
    y="probability_of_default_pd",
    size="expected_loss_el",
    title="Financial Stress vs Probability of Default"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)