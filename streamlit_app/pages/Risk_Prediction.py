import streamlit as st

st.title("🧠 Explainable AI")

st.write("""
SHAP helps explain why a customer receives a high or low risk score.
""")

try:
    st.image(
        "reports/shap_summary.png"
    )
except:
    st.warning(
        "Generate shap_summary.png from model evaluation notebook."
    )