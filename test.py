import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import pytz
import ta

def fetch_Stock_data(ticker, period, interval):
    end_date = datetime.now()
    if period == "1wk":
        start_date = end_date - timedelta(days=7)
        data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    else:
        data = yf.download(ticker, period=period, interval=interval)
    return data

def process_data(data):
    if data.index.tzinfo is None:
        data.index = data.index.tz_localize("UTC")
    data.index = data.index.tz_convert("US/Eastern")
    data.reset_index(inplace=True)
    data.rename(columns={"Date": "Datetime"}, inplace=True)
    return data


def add_technical_indicators(data):
    data["SMA_20"] = ta.trend.sma_indicator(data["Close"].squeeze(), window=20)
    data["EMA_20"] = ta.trend.ema_indicator(data["Close"].squeeze(), window=20)
    return data


def calculate_metrics(data):
    last_close = data["Close"].iloc[-1].item()
    prev_close = data["Close"].iloc[0].item()
    change = last_close - prev_close
    pct_change = (change / prev_close) * 100
    high = data["High"].max().item()
    low = data["Low"].min().item()
    volume = data["Volume"].sum().item()
    return last_close, change, pct_change, high, low, volume


data = fetch_Stock_data("AAPL", "1d", "1m")
print(data)

data = process_data(data)
print(data)

# last_price = data["Close"].iloc[-1].item()
# print(last_price)

# print(data["Close"].squeeze())

data = add_technical_indicators(data)
print(data)

last_close, change, pct_change, high, low, volume = calculate_metrics(data)

print(f"{last_close:.2f}, {change:.2f}, {pct_change:.2f}, {high:.2f}, {low:.2f}, {volume:.2f}")