
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def MarvellousCalculateKNN():
    border = "*"*50

    data  = pd.read_csv("WinePredictor.csv")
    print("\n",border)
    print("\n Volume of data set is :" ,len(data) ,"Features are 13")

    print(data,"\n")
    print(border,"\n")

    Target  = data.Class
    Data_train,Data_test,Target_train,Target_test = train_test_split(data,Target,test_size =0.5)

    print("Data is split for traning is \n")
    print(Data_train,"\n")
    print(border)

    print("Data is split for testing is \n")
    print(Data_test,"\n")
    print(border)

    classifier = KNeighborsClassifier()
    classifier.fit(Data_train,Target_train)

    predictions = classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test,predictions)
    print("\nAccuracy Using KNN is : ", Accuracy * 100, "%")

    print(border)

def main():
    print("__________________________________________________________________")
    print("--------------MAchine learning application----------")
    print("Wine predictor application using K nearest Kneighbor alogorithm")

    MarvellousCalculateKNN()

if __name__ == "__main__":
    main()