import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st
import datetime



def app():
    # start = '2010-01-01'
    # end = '2019-12-31'

    st.markdown('''
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap" rel="stylesheet">
        </head>
        
        <h1 style="font-family: 'Permanent Marker', cursive;font-size:60px;text-align:center;margin-top:0;margin-bottom:0;padding-top:0">STOCKZU</h1>
        <p style="font-family: 'Lato', sans-serif;text-align:right;font-style:italic;margin-bottom:2rem;">~ The future is something to build!</p>
        ''',True)

    user_input = st.text_input('Enter Stock Ticker', 'AAPL')
    start = st.date_input(
     "Enter the Start Date",
     datetime.date(2010, 1, 1))

    end = st.date_input(
     "Enter the End Date",
     datetime.date(2019, 12, 31))

    
    st.markdown('''
        <br>
        ''',True)



    df = data.DataReader(user_input,'yahoo',start,end)

    
    st.write(df.describe())

    st.markdown('''
        <hr style="padding:0;border-style: dotted none none;border-color: white;border-width: 5px;width: 10%;margin: 2rem auto;">    
    ''',True)