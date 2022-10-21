import yfinance as yf
import streamlit as st
from symbol_list import symbol_list_2

with st.sidebar:
    options = st.multiselect(
        "Choose currency",
        symbol_list_2
    )

options = ["BTC-USD", "ETH-USD", "ADA-USD"]

def create_symbol_data():
    for symbol in options:
        currency = yf.Ticker(symbol)
        print(currency)
        print(currency.info)

create_symbol_data()

