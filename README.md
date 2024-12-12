# Stock Analysis Dashboard

## Overview
The **Stock Analysis Dashboard** is an interactive web application built using Streamlit. It allows users to analyze stock data, visualize historical trends, and calculate technical indicators such as SMA (Simple Moving Average) and EMA (Exponential Moving Average). The app also provides real-time stock metrics for popular stocks like AAPL, GOOGL, AMZN, and MSFT.

---

## Features
- **Stock Data Visualization**: Fetch and visualize stock data using candlestick and line charts.
- **Technical Indicators**: Add SMA (20) and EMA (20) indicators to your analysis.
- **Real-Time Metrics**: Display real-time stock prices, price changes, and percentage changes for selected stocks.
- **Historical Data**: View detailed historical stock data with columns such as Open, High, Low, Close, and Volume.

---

## Requirements

### Python Libraries
The application requires the following Python libraries:
- `streamlit`
- `plotly`
- `pandas`
- `yfinance`
- `ta`
- `pytz`

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

---

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repository>.git
   cd <your-repository>
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Open your browser and go to `http://localhost:8501` to view the app.

---

## Deployment on Streamlit Community Cloud
1. Push your code to a GitHub repository.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud) and log in with your GitHub account.
3. Select your repository and configure the app settings (e.g., set `app.py` as the main file).
4. Deploy the app and share the generated link.

---

## Usage
### Sidebar Options
- **Ticker**: Enter the stock symbol (e.g., `AAPL`, `GOOGL`).
- **Time Period**: Select from `1d`, `1wk`, `1mo`, `1yr`, or `max`.
- **Chart Type**: Choose between candlestick or line chart.
- **Technical Indicators**: Select `SMA 20` or `EMA 20` to overlay on the chart.

### Real-Time Prices
View the real-time price changes and percentage movements of predefined stocks (AAPL, GOOGL, AMZN, MSFT).

---

## Example Screenshots
- **Candlestick Chart with SMA and EMA:**
  Visualize historical price movements with technical indicators overlaid.

- **Real-Time Stock Prices:**
  Monitor the latest stock performance in the sidebar.

---

## About
This project was developed to provide an easy-to-use interface for stock data analysis, catering to both casual investors and financial analysts.

---


## Contributing
Contributions are welcome! If you'd like to improve the app, feel free to fork the repository and submit a pull request.

---

## Contact
For any questions or feedback, please contact:
- **Developer**: Chandan Kumar
- **Email**: chandan_6903@proton.me

---

