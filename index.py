import streamlit as st
from multiapp import MultiApp
from apps import home,data, closetime,hundred, twohundred, predictor



app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Closing Price VS Time Chart", closetime.app)
app.add_app("Closing Price vs Time Chart with 100MA", hundred.app)
app.add_app("Closing Price vs Time Chart with 100MA & 200MA", twohundred.app)
app.add_app("Stock Predictor", predictor.app)
app.add_app("Summary", data.app)

app.run()