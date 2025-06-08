import yfinance as yf
import pandas as pd
import numpy as np

def fetch_data(symbol):
    df = yf.download(symbol, interval="1m", period="1d")
    df.dropna(inplace=True)
    return df

def extract_features(df):
    df['return'] = df['Close'].pct_change()
    last = df.iloc[-15:]  # Пример: последние 15 минут
    features = [
        last['return'].mean(),
        last['High'].max() - last['Low'].min(),
        last['Close'].iloc[-1] - last['Open'].iloc[0]
    ]
    return features
