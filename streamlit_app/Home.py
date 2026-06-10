import streamlit as st
import pandas as pd
import os

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Finance Risk Intelligence",
    page_icon="📊",
    layout="wide"
)

# =====================================
# DATA LOADING
# =====================================

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "final_features.csv"
)

df = pd.read_csv(DATA_PATH)

# =====================================
# KPIs
# =====================================

total_customers = len(df)

avg_pd = round(
    df["probability_of_default_pd"].mean() * 100,
    2
)

avg_lgd = round(
    df["loss_given_default_lgd"].mean() * 100,
    2
)

portfolio_loss = round(
    df["expected_loss_el"].sum(),
    0
)

# =====================================
# HEADER
# =====================================

st.title("🏦 Finance Risk Intelligence")

st.markdown("""
### AI-Powered Credit Risk Analytics Platform

A complete Credit Risk Analytics solution combining:

- Data Analytics
- Machine Learning
- Explainable AI (SHAP)
- Business Intelligence
- Risk Portfolio Monitoring
""")

# =====================================
# KPI CARDS
# =====================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Customers",
        f"{total_customers:,}"
    )

with col2:
    st.metric(
        "Average PD",
        f"{avg_pd}%"
    )

with col3:
    st.metric(
        "Average LGD",
        f"{avg_lgd}%"
    )

with col4:
    st.metric(
        "Portfolio Loss",
        f"${portfolio_loss:,.0f}"
    )

st.divider()

# =====================================
# DATASET PREVIEW
# =====================================

st.subheader("Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

# =====================================
# PROJECT OVERVIEW
# =====================================

st.subheader("Project Overview")

st.write("""
This project predicts borrower risk using machine learning models such as:

• Logistic Regression

• Decision Tree

• Random Forest

• XGBoost

• CatBoost

The system evaluates:

- Probability of Default (PD)
- Loss Given Default (LGD)
- Expected Loss (EL)
- Portfolio Risk Exposure

and supports data-driven lending decisions.
""")

