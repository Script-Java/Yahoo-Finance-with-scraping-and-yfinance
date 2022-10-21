import yfinance as yf
from list import symbol_list
import streamlit as st
import pprint

st.write("YFinance with python")
st.write("Choose some tickers on the sidebar to get started")

with st.sidebar:
  options = st.multiselect("Symbol Tickers", symbol_list)


def get_ticker_data(options):
  for tickers in options:
    ticks = yf.Ticker(tickers)
    data = ticks.info
    name = data["shortName"]
    price = data["regularMarketPrice"]
    description = data["description"]
    col1, col2, col3 = st.columns(3)
    col1.metric("Name", name, "")
    col2.metric("Price", price, "")
    col3.metric("Description", description, "")
    


if options != []:
  get_ticker_data(options)
