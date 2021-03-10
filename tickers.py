import numpy as np
import pandas as pd
import hvplot.pandas 
from pathlib import Path
import yfinance as yf
import streamlit as st 

new_ticker = str(st.text_input("enter ticker"))
name = yf.Ticker(new_ticker)

square_1d_2year = name.history(start='2018-12-23', end='2021-03-08', interval='1d' )

signals_df = square_1d_2year.drop(columns=['Open', 'High', 'Low', 'Volume','Dividends', 'Stock Splits'])

short_window = 50
long_window = 100

signals_df['SMA50'] = signals_df['Close'].rolling(window=short_window).mean()
signals_df['SMA100'] = signals_df['Close'].rolling(window=long_window).mean()
signals_df['Signal'] = 0.0

signals_df['Signal'][short_window:] = np.where(
    signals_df['SMA50'][short_window:] > signals_df['SMA100'][short_window:], 1.0, 0.0
)
signals_df['Entry/Exit'] = signals_df['Signal'].diff()
signals_df.tail(10)

# Visualizing exit position relative to close price
exit = signals_df[signals_df['Entry/Exit'] == -1.0]['Close'].hvplot.scatter(
    color='red',
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)
# Visualize entry position relative to close price
entry = signals_df[signals_df['Entry/Exit'] == 1.0]['Close'].hvplot.scatter(
    color='green',
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)
# Visualize close price for the investment
security_close = signals_df[['Close']].hvplot(
    line_color='grey',
    ylabel='Price in $',
    width=1000,
    height=400
)
# Visualize moving averages
moving_avgs = signals_df[['SMA50', 'SMA100']].hvplot(
    ylabel='Price in $',
    width=1000,
    height=400
)
# Overlay plots
entry_exit_plot = security_close * moving_avgs * entry * exit
entry_exit_plot.opts(xaxis=None)

price_df = signals_df[['Close', 'SMA50', 'SMA100']]
price_chart = price_df.hvplot.line()
price_chart.opts(title='Square', xaxis=None)

def main():
    
    st.dataframe(signals_df.tail(10))
    st.line_chart(price_df)

    
main()