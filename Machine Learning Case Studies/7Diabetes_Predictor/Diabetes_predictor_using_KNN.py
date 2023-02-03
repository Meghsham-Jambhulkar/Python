import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def main():
    print("-----Diabetes predictor using K Nearest Neighnpurs-----")
    diabetes = pd.read_csv('diabetes.csv')
    print("Columns of Dataset : ",diabetes.columns)
    print("Dimesnsions of the diabetes data {}".format(diabetes.shape))
     
    X_train , X_test , Y_train , Y_test = train_test_split(diabetes.loc[:,diabetes.columns != 'Outcome']
    ,diabetes['Outcome'],
    stratify=diabetes['Outcome'],
    random_state=66)

    training_accuracy = {}
    test_accuracy = {}
    #dictname[key] = value

    neighbors_settings = range(1,11)
    
    for n_neighbors in neighbors_settings:
        knn = KNeighborsClassifier(n_neighbors=n_neighbors)
        knn.fit(X_train, Y_train)
        training_accuracy[n_neighbors]=(knn.score(X_train,Y_train))*100

        test_accuracy[n_neighbors] = (knn.score(X_test, Y_test))*100

    print("Training Accuracy for each neighbour ",training_accuracy)
    print("Test Accuracy for each neighbour ",test_accuracy)

    plt.plot(neighbors_settings,list(training_accuracy.values()),label="Training Accuracy")
    plt.plot(neighbors_settings,list(test_accuracy.values()),label="Test Accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("No. of Numbers")
    plt.legend()
    plt.savefig('knn_compare_model')
    plt.show()

    knn = KNeighborsClassifier(n_neighbors=9)
    knn.fit(X_train,Y_train)

    print("Accuracy of K-NN classifier on training set :{:.2f}".format(knn.score(X_train, Y_train)*100))
    print("Accuracy of K-NN classifier on test set :{:.2f}".format(knn.score(X_test, Y_test)*100))










if __name__ == "__main__":
    main()