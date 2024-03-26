# Encoding for Weather:
# Overcast: 0
# Rainy: 1
# Sunny: 2

# Encoding for Temperature:
# Cool: 0
# Hot: 1
# Mild: 2



import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def PlayPredictor(data_path):
    data = pd.read_csv(data_path)
    print("Actual size of dataset ", len(data))

    feature_names = ['Weather', 'Temperature']
    print("Name of the features ", feature_names)

    features = data[feature_names]
    label = data['Play']

    le = preprocessing.LabelEncoder()

    # Fit and transform all categorical features together
    features_encoded = features.apply(le.fit_transform)


    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(features_encoded, label)

    # Predict for a new data point
    user_weather = input("Enter weather (Sunny, Overcast, Rainy): ").capitalize()
    user_temp = input("Enter temperature (Hot, Mild, Cool): ").capitalize()

    if user_weather == 'Overcast':
        user_weather_encoded = 0
    elif user_weather == 'Rainy':
        user_weather_encoded = 1
    elif user_weather == 'Sunny':
        user_weather_encoded = 2

        
    if user_temp == 'Cool':
        user_temp_encoded = 0
    elif user_temp == 'Hot':
        user_temp_encoded = 1
    elif user_temp == 'Mild':
        user_temp_encoded = 2

    predicted = model.predict([[user_weather_encoded, user_temp_encoded]])
    print("Predicted label:", predicted[0])

def main():
    print("----------Play Predictor Case Study----------")
    print("Machine Learning Application")

    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()
