import streamlit as st
import pprint

st.write("YFinance with python made by Atrin Shahroudi")
st.markdown("Made with ```-Streamlit``` ```-yFinance``` ```-BeautifulSoup```")
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
        link = data["coinMarketCapLink"]
        col1, col2 = st.columns(2)
        col1.metric("Name", name, "")
        col2.metric("Price", price, "")
        st.write(description)
        st.write(link)
        graph_data = yf.download(tickers, start="2021-11-18", end="2022-10-21")
        history = ticks.history(period=max)
        st.write(history)
        st.bar_chart(graph_data)

if options != []:
    get_ticker_data(options)
