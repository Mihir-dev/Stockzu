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

    df = data.DataReader(user_input,'yahoo',start,end)

    #Splitting Data into training and testing

    data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
    data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0,1))

    data_training_array = scaler.fit_transform(data_training)


    #Load My Model

    model = load_model('C:/Users/Mihir Thotam/Desktop/Stock-Price/apps/keras_model.h5')

    past_100_days =  data_training.tail(100)
    final_df = past_100_days.append(data_testing, ignore_index=True)


    input_data = scaler.fit_transform(final_df)


    x_test = []
    y_test = []

    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i-100: i])
        y_test.append(input_data[i,0])

    x_test, y_test = np.array(x_test), np.array(y_test)

    y_predicted = model.predict(x_test)

    scaler = scaler.scale_

    scale_factor = 1/scaler[0]
    y_predicted = y_predicted * scale_factor
    y_test = y_test * scale_factor

    #Final Graph

    st.subheader('Predictions VS Original')

    st.markdown('''
        <br>
        ''',True)
        
    fig2 = plt.figure(figsize=(12,6))
    plt.plot(y_test, 'b', label = 'Origninal Price')
    plt.plot(y_predicted, 'r', label='Predicted Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(fig2)

    st.markdown('''
        <hr style="padding:0;border-style: dotted none none;border-color: white;border-width: 5px;width: 10%;margin: 2rem auto;">    
    ''',True)