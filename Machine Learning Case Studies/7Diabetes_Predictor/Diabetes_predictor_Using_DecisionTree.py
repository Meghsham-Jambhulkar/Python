import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    print("-----Diabetes Predictor Using Decision Tree-----")
    
    diabetes = pd.read_csv('diabetes.csv')
    print("Columns of the Dataset")
    print(diabetes.columns)

    print("Dimensions of Diabetes data :{}".format(diabetes.shape))

    X_train , X_test , Y_train , Y_test = train_test_split(diabetes.loc[:,diabetes.columns != 'Outcome']
    ,diabetes['Outcome'],
    stratify=diabetes['Outcome'],
    random_state=66)
    tree = DecisionTreeClassifier(random_state=0)
    tree.fit(X_train,Y_train)
    print("Accuracy on training set : {:.2f}%".format((tree.score(X_train, Y_train))*100))

    print("Accuracy on test set :{:.3f}%".format(tree.score(X_test,Y_test)*100))

    tree = DecisionTreeClassifier(max_depth=5,random_state=0)
    tree.fit(X_train,Y_train)
    print("Accuracy on training set : {:.2f}%".format((tree.score(X_train, Y_train))*100))

    print("Accuracy on test set :{:.3f}%".format(tree.score(X_test,Y_test)*100))

    print("Features importances :\n{}".format(tree.feature_importances_))

    def plot_feature_importance(model):
        plt.figure(figsize=(8,6))
        n_features = 8
        plt.barh(range(n_features),model.feature_importances_,align='center')
        diabetes_features = [x for i , x in enumerate(diabetes.columns) if i != 8 ]
        plt.yticks(np.arange(n_features),diabetes_features)
        plt.ylabel("Features")
        plt.xlabel("Feature Importance")
        plt.ylim(-1,n_features)
        plt.savefig(fname="Feature_Importance using Tree")
        plt.show()

    plot_feature_importance(tree)
    






if __name__ =="__main__":
    main()