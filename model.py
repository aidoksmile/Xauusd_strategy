import joblib
import numpy as np

def load_model():
    return joblib.load("models/xgb_model.joblib")

def predict_signal(model, features):
    prediction = model.predict(np.array([features]))[0]
    return "buy" if prediction == 1 else "sell"