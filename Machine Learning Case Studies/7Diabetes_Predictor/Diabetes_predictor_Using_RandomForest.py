import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from warnings import simplefilter



def main():
    simplefilter(action = 'ignore',category = FutureWarning)
    print("-----Diabetes Predictor Using Decision Random Forest-----")
    
    diabetes = pd.read_csv('diabetes.csv')
    print("Columns of the Dataset")
    print(diabetes.columns)

    print("Dimensions of Diabetes data :{}".format(diabetes.shape))

    X_train , X_test , Y_train , Y_test = train_test_split(diabetes.loc[:,diabetes.columns != 'Outcome']
    ,diabetes['Outcome'],
    stratify=diabetes['Outcome'],
    random_state=66)
    
    rf = RandomForestClassifier(n_estimators=100,random_state=0)
    rf.fit(X_train,Y_train)
    print("Accuracy on training set : {:.2f}%".format((rf.score(X_train, Y_train))*100))

    print("Accuracy on test set :{:.3f}%".format(rf.score(X_test,Y_test)*100))

    rf = RandomForestClassifier(max_depth=5,n_estimators = 100 ,random_state=0)
    rf.fit(X_train,Y_train)
    print("Accuracy on training set : {:.2f}%".format((rf.score(X_train, Y_train))*100))

    print("Accuracy on test set :{:.3f}%".format(rf.score(X_test,Y_test)*100))

    
    def plot_feature_importance(model):
        plt.figure(figsize=(8,6))
        n_features = 8
        plt.barh(range(n_features),model.feature_importances_,align='center')
        diabetes_features = [x for i , x in enumerate(diabetes.columns) if i != 8 ]
        plt.yticks(np.arange(n_features),diabetes_features)
        plt.ylabel("Features")
        plt.xlabel("Feature Importance")
        plt.ylim(-1,n_features)
        plt.savefig(fname="Feature_Importance using Random Forest")
        plt.show()

    plot_feature_importance(rf)

if __name__ =="__main__":
    main()