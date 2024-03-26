import streamlit as st
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def play_predictor():
    st.title("Play Predictor")
    st.write("Machine Learning Application")

    @st.cache_data
    def load_data():
        data = pd.read_csv("PlayPredictor.csv")
        return data

    data = load_data()

    feature_names = ['Weather', 'Temperature']
    features = data[feature_names]
    label = data['Play']

    le = preprocessing.LabelEncoder()
    features_encoded = features.apply(le.fit_transform)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(features_encoded, label)

    user_weather = st.selectbox("Select weather", ['Sunny', 'Overcast', 'Rainy'])
    user_temp = st.selectbox("Select temperature", ['Hot', 'Mild', 'Cool'])

    user_weather_encoded = {'Overcast': 0, 'Rainy': 1, 'Sunny': 2}
    user_temp_encoded = {'Cool': 0, 'Hot': 1, 'Mild': 2}

    user_weather_code = user_weather_encoded[user_weather]
    user_temp_code = user_temp_encoded[user_temp]

    predicted = model.predict([[user_weather_code, user_temp_code]])

    if predicted[0] == 'Yes':
        st.success("You should play!")
    else:
        st.error("Better not to play.")

if __name__ == "__main__":
    play_predictor()
