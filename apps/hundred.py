import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st
import plotly.express as px
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

    df = data.DataReader(user_input,'yahoo',start,end)

    st.subheader('Closing Price vs Time Chart with 100MA')

    graph = st.selectbox("What kind of Graph ?", ["Non-Interactive Graph", "Interactive Graph"])

    if graph == "Non-Interactive Graph":
        st.markdown('''
        <br>
        ''',True)
        ma100 = df.Close.rolling(100).mean()
        fig = plt.figure(figsize = (12,6))
        plt.plot(ma100)
        plt.plot(df.Close)
        st.pyplot(fig)

    if graph == "Interactive Graph":
        st.markdown('''
        <br>
        ''',True)
        ma100 = df.Close.rolling(100).mean()
        fig1 = px.line(df,y = [ma100,df.Close],title="Closing Price vs Time Chart with 100MA")
        st.plotly_chart(fig1)

    
    st.markdown('''
        <hr style="padding:0;border-style: dotted none none;border-color: white;border-width: 5px;width: 10%;margin: 2rem auto;">    
    ''',True)