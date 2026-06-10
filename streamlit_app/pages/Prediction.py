import streamlit as st

st.title("Risk Prediction")

st.info(
    "Prediction module currently under development."
)

age = st.number_input(
    "Age",
    18,
    100,
    30
)

income = st.number_input(
    "Monthly Income",
    1000,
    100000,
    50000
)

if st.button("Predict"):

    st.success(
        "Prediction pipeline working."
    )