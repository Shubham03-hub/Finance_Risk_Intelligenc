import pandas as pd
import joblib
import shap

df = pd.read_csv("../data/dataset.csv")

X = df.drop("target", axis=1)

model = joblib.load("../models/xgb_model.pkl")

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

shap.summary_plot(shap_values, X)