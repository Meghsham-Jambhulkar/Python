import math
import numpy as np 
import pandas as pd 
#from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 

def MarvellousTitanicLogistic():
    titanic_data = pd.read_csv('titanic.csv')
    print("First 5 Entries from Loaded dataset ")
    print(titanic_data.head())

    print("Number of Passangers are : "+str(len(titanic_data)))

    print("Visulisation : survived or non survived passangers")
    figure()
    target= "Survived"

    # countplot(data=titanic_data , x = target).set_title("Survived or Non survived ")
    # plt.savefig("1.png",dpi=300, bbox_inches='tight')
    # show()

    # print("Visualisation : survived based on Gender")
    # countplot(data=titanic_data , x = target,hue = "Sex").set_title("Survived or Non survived based on Gender")
    # plt.savefig("2.png",dpi=300, bbox_inches='tight')
    # show()

    # print("Visualisation : Survived and non survived passengers based on passanger class")
    # figure()
    # target = "Survived"
    # countplot(data= titanic_data , x = target , hue = "Pclass").set_title("Survived and non survived passengers based on passanger class")
    # plt.savefig("3.png",dpi=300, bbox_inches='tight')
    # show()

    print("Visualisation : Survived and non survived based on Age ")
    figure()
    titanic_data["Age"].plot.hist().set_title("Survived and non survived based on Age")
    plt.savefig("4.png",dpi=300, bbox_inches='tight')
    show()

    print("Visualisation : Survived and non survived based on Fare ")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Survived and non survived based on Fare")
    plt.savefig("5.png",dpi=300, bbox_inches='tight')
    show()

    titanic_data.drop("zero", axis=1 , inplace = True)

    print("First 5 entries from loaded data after removing zero column ")
    print(titanic_data.head(5))

    print("Values of sex column ")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("Values of Sex Column after removing one field ")
    Sex = pd.get_dummies(titanic_data["Sex"], drop_first = True )
    print(Sex.head(5))

    print("Values of Sex coumn after removing one field")
    Pclass = pd.get_dummies(titanic_data["Pclass"],drop_first = True)
    print(Pclass.head(5))

    print("Values of data set after concatenating new columns ")
    titanic_data = pd.concat([titanic_data,Sex,Pclass],axis = 1)
    print(titanic_data.head(5))

    print("Values of data set after removing irrelevant columns ")
    titanic_data.drop(["Sex","SibSp","Parch","Embarked"],axis = 1,inplace = True)
    print(titanic_data.head(5))

    x = titanic_data.drop("Survived",axis = 1)
    y = titanic_data["Survived"]

    xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size =0.5)

    logmodel = LogisticRegression()

    logmodel.fit(xtrain,ytrain)

    prediction = logmodel.predict(xtest)

    print("Classification Report of Logistic Regression is : ")
    print(classification_report(ytest,prediction))

    print("Confusion Matrix of Logistic Regression is :")
    print(confusion_matrix(ytest ,prediction))

    print("Accuracy of Logistic Regression is :")
    print(accuracy_score(ytest , prediction ))

def main():
    print("--------------TITANIC PREDICTION------------")

    print("Logistic Regression of Titanic Dataset ")

    MarvellousTitanicLogistic()


if __name__ == "__main__":
    main()
















