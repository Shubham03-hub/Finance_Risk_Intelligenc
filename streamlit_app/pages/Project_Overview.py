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

st.title("Project Overview")

st.header("Business Problem")

st.write("""
Banks lose millions due to risky lending decisions.

The goal is to predict customer default risk before approving loans.
""")

st.header("Business Objectives")

st.write("""
- Reduce credit losses
- Improve loan approval decisions
- Increase portfolio profitability
- Automate risk scoring
""")

st.header("Project Architecture")

st.code("""
Raw Data
 ↓
Cleaning
 ↓
EDA
 ↓
Feature Engineering
 ↓
Machine Learning
 ↓
Model Evaluation
 ↓
Explainable AI
 ↓
Dashboard
 ↓
Deployment
""")