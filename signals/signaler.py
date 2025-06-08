from models.model import load_model, predict_signal
from utils.data import fetch_data, extract_features
from utils.webhook import send_signal

def analyze_and_signal():
    df = fetch_data("XAUUSD")
    features = extract_features(df)
    model = load_model()
    signal = predict_signal(model, features)
    send_signal(signal)
