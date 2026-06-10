from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("../models/xgb_model.pkl")
threshold = np.load("../models/best_threshold.npy")

@app.post("/predict")
def predict(data: dict):

    features = np.array(list(data.values())).reshape(1, -1)

    prob = model.predict_proba(features)[0][1]
    pred = int(prob >= threshold)

    return {
        "probability": float(prob),
        "prediction": pred
    }