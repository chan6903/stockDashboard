import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Sample data (replace with your actual data)
data = pd.DataFrame({
    'Datetime': ['2023-12-01 09:00', '2023-12-01 10:00', '2023-12-01 11:00'],
    'Open': [100, 105, 110],
    'High': [110, 115, 120],
    'Low': [95, 100, 105],
    'Close': [108, 112, 118]
})
data['Datetime'] = pd.to_datetime(data['Datetime'])

# Create the candlestick chart
fig = go.Figure()
fig.add_trace(go.Candlestick(
    x=data['Datetime'],
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close']
))

# Set chart layout
fig.update_layout(
    title="Candlestick Chart",
    xaxis_title="Datetime",
    yaxis_title="Price",
    xaxis_rangeslider_visible=False
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
