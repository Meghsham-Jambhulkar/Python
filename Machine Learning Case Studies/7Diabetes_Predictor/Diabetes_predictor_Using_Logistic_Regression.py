import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from warnings import simplefilter


def main():
    simplefilter(action = 'ignore',category = FutureWarning)

    print("-----Diabetes Predictor Using Decision Logistic Regression-----")
    
    diabetes = pd.read_csv('diabetes.csv')
    print("Columns of the Dataset")
    print(diabetes.columns)

    print("Dimensions of Diabetes data :{}".format(diabetes.shape))

    X_train , X_test , Y_train , Y_test = train_test_split(diabetes.loc[:,diabetes.columns != 'Outcome']
    ,diabetes['Outcome'],
    stratify=diabetes['Outcome'],
    random_state=66)

    logreg = LogisticRegression()
    logreg.fit(X_train,Y_train)
    print("Accuracy on training set : {:.2f}%".format((logreg.score(X_train, Y_train))*100))

    print("Accuracy on test set :{:.3f}%".format(logreg.score(X_test,Y_test)*100))

    logreg = LogisticRegression(C=0.01)
    logreg.fit(X_train,Y_train)
    print("Accuracy on training set : {:.2f}%".format((logreg.score(X_train, Y_train))*100))

    print("Accuracy on test set :{:.3f}%".format(logreg.score(X_test,Y_test)*100))

if __name__ =="__main__":
    main()