
import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

#Sunny = 1 
#Overcast = 2
#Rainy = 3

#Hot = 1
#Mild = 2
#Cool =3

#Yes = 1
#No = 0

# Assigning features and label variables
# First Feature

def PlayPredictor(data_path,weat,temp):
    data = pd.read_csv(data_path , index_col=0)
    print("Size of actual dataset is ",len(data))
    features_names = ['Weather' , 'Temperature']
    print("Names of the Features :",features_names)

    weather = data.Weather
    Temperature = data.Temperature

    play = data.Play

    le = preprocessing.LabelEncoder()

    Weather_Encoded = le.fit_transform(weather)

    temp_Encoded = le.fit_transform(Temperature)

    Label = le.fit_transform(play)


    features = list(zip(Weather_Encoded,temp_Encoded))

    model = KNeighborsClassifier()

    model.fit(features,Label)

    predicted = model.predict([[weat,temp]])


    return predicted



    




def main():

    print("----------Playy Predictor Case Study----------")
    print("Enter the weather (Sunny / Overcast / Rainy) :")
    weather = input()
    print("Enter the type of Temperature of your (Hot  / Mild / Cool)")
    Temperature = input()
    if weather.lower()=="sunny":
        weather = 2
    elif weather.lower()=="overcast":
        weather = 0
    elif weather.lower()=="rainy":
        weather = 1
    else :
        print("Invalid type of Weather ")
        exit()

    if Temperature.lower()=="hot":
        Temperature = 1
    elif Temperature.lower()=="mild":
        Temperature = 2
    elif Temperature.lower()=="cool":
        Temperature = 0
    else :
        print("Invalid type of Temperature ")
        exit()


    Play = PlayPredictor("PlayPredictor.csv",weather,Temperature)
    if Play == 1 :
        print("You Can Play")
    else :
        print("You Should Not Play")

if __name__ == "__main__":
    main()