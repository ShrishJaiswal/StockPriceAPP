import streamlit as st
from datetime import date

import yfinance as yf
import pandas as pd
import datetime

st.markdown('''
# Stock Price APP
''')

st.write('---')

# Sidebar
st.sidebar.subheader('Input Parameters')
start_date=st.sidebar.date_input('Start Date',datetime.date(2022,1,1))
end_date=st.sidebar.date_input('End Date',datetime.date(2022,6,7))

# Ticker Data
ticker_lst=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_lst) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)
print(type(tickerDf))

# Graph of Closing Price
st.header('Stock Price')
st.line_chart(tickerDf.Close)


# Bar Chart of Closing Price
st.header('Stock Price')
st.bar_chart(tickerDf.Close)
