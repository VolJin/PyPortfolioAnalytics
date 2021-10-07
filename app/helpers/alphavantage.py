import streamlit as st
from alpha_vantage.timeseries import TimeSeries

class av:
    try:
        ts = TimeSeries(key=st.secrets['AV_API_KEY'], output_format='pandas', indexing_type='date')

    except ValueError:
        print('Please provide a valid AlphaVantage API key.\nGet a free key from https://www.alphavantage.co/support/#api-key')
