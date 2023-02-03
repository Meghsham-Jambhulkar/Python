#Sunny = 1
#Overcast = 2
#Rainy = 3

#Hot = 1
#Mild = 2
#Cool = 3

#Yes = 1
#No = 2



import numpy as np 
import pandas as pd 
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def PlayPredictor(data_path):

    data = pd.read_csv(data_path,index_col = 0)

    print("Actual size of dataset ",len(data))

    feature_names = ['Weather','Temperature']

    print("Name of the features ",feature_names)

    weather = data.Weather
    temperature = data.Temperature

    play = data.Play

    le = preprocessing.LabelEncoder()

    weather_encoded = le.fit_transform(weather)

    temp_encoded = le.fit_transform(temperature)

    label = le.fit_transform(play)

    features = list(zip(weather_encoded , temp_encoded))
    model = KNeighborsClassifier(n_neighbors = 3)

    model.fit(features,label)
    predicted = model.predict([[0,2]])

    print(predicted)

def main():

    print("----------Play Predictor Case Study----------")
    print("Machine Learning Application")

    PlayPredictor("PlayPredictor.csv")


if __name__ == "__main__":
    main()