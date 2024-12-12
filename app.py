import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf
from datetime import datetime, timedelta
import pytz
import ta 


st.set_page_config(layout="wide")
st.title("Stock Analysis Interface")



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

def calculate_metrics(data):
    last_close = data["Close"].iloc[-1].item()
    prev_close = data["Close"].iloc[0].item()
    change = last_close - prev_close
    pct_change = (change / prev_close) * 100
    high = data["High"].max().item()
    low = data["Low"].min().item()
    volume = data["Volume"].sum().item()
    return last_close, change, pct_change, high, low, volume

def add_technical_indicators(data):
    data["SMA_20"] = ta.trend.sma_indicator(data["Close"].squeeze(), window=20)
    data["EMA_20"] = ta.trend.ema_indicator(data["Close"].squeeze(), window=20)
    return data



st.sidebar.header("Chart Parameters")
ticker = st.sidebar.text_input("Ticker", "ADBE")
time_period = st.sidebar.selectbox("Time Period", ["1d", "1wk", "1mo", "1yr", "max"])
chart_type = st.sidebar.selectbox("Chart Type", ["Candlestick", "Line"])
indicators = st.sidebar.multiselect("Technical Indicators", ["SMA 20", "EMA 20"])



interval_mapping = {
    "1d": "1m",
    "1wk": "30m",
    "1mo": "1d",
    "1yr": "1wk",
    "max": "1wk"
}




if st.sidebar.button("Update"):
    data = fetch_Stock_data(ticker, time_period, interval_mapping[time_period])
    data = process_data(data)
    data = add_technical_indicators(data)

    last_close, change, pct_change, high, low, volume = calculate_metrics(data)

    st.metric(label=f"{ticker} Last Price", value=f"{last_close:.2f} USD", delta=f"{change:.2f} ({pct_change:.2f}%)")

    col1, col2, col3 = st.columns(3)

    col1.metric("High", f"{high:.2f} USD")
    col2.metric("Low", f"{low:.2f} USD")
    col3.metric("Volume", f"{volume:.2f}")

    fig = go.Figure()
    if chart_type == "Candlestick":
        data['Datetime'] = pd.to_datetime(data['Datetime'])
        fig.add_trace(go.Candlestick(x=data['Datetime'],open=data['Open'],high=data['High'],low=data['Low'],close=data['Close']))

    else:
        fig = px.line(data, x="Datetime", y = data["Close"].squeeze())

    for indicator in indicators:
        if indicator == "SMA 20":
            fig.add_trace(go.Scatter(x=data["Datetime"], y=data["SMA_20"], name="SMA 20"))
        elif indicator == "EMA 20":
            fig.add_trace(go.Scatter(x=data["Datetime"], y=data["EMA_20"], name="EMA 20"))
    
    fig.update_layout(title=f"{ticker} {time_period.upper()} Chart",
                      xaxis_title = "Time",
                      yaxis_title = "Price (USD)",
                      height = 600)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Historical Data")
    st.dataframe(data[["Datetime", "Open", "High", "Low", "Close", "Volume"]])

    st.subheader("Technical Indicators")
    st.dataframe(data[["Datetime", "SMA_20", "EMA_20"]])






st.sidebar.header("Real Time Stock Prices")
stock_symbols = ["AAPL", "GOOGL", "AMZN", "MSFT"]
for symbol in stock_symbols:
    real_time_data = fetch_Stock_data(symbol, "1d", "1m")
    if not real_time_data.empty:
        real_time_data = process_data(real_time_data)
        last_price = real_time_data["Close"].iloc[-1].item()
        change = last_price - real_time_data["Open"].iloc[0].item()
        pct_change = (change / real_time_data["Open"].iloc[0]).item() * 100
        st.sidebar.metric(f"{symbol}", f"{last_price:.2f} USD", f"{change:.2f} ({pct_change:.2f}%)")




st.sidebar.subheader("About")
st.sidebar.info("This project was developed to provide an easy-to-use interface for stock data analysis, catering to both casual investors and financial analysts.")