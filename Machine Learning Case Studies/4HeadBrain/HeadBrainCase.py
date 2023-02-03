import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

def HeadBrainPredictor(data_path):

    data = pd.read_excel(data_path)

    print("Size of data set ",data.shape)

    X = data["Head Size (cm^3)"].values
    Y = data["Brain Weight (grams)"].values

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator += (X[i]-mean_x) * (Y[i] - mean_y)
        denominator += (X[i]-mean_x) ** 2

        m = numerator / denominator

        c = mean_y - (m * mean_x)

        print("Slope of Regression line ",m)
        print("Y intercept of Regression line ",c)

        max_x = np.map(X)+100
        min_x = np.min(X)-100

        x = np.linspace(min_x,max_x , n)

        y = c + m * x 
        plt.plot(x , y , color = '#58b970' , label = 'Regression Line')
        plt.plot(X , Y , color = '#ef5423' , label = 'scatter plot')
        plt.xlabel("Head Size in cm^3")
        plt.ylabel("Brain Weight in grams")

        plt.legend()
        plt.savefig()
        plt.show()

        ss_t = 0
        ss_r = 0

        for i in range(n):
            y_pred = c + m * X[i]
            ss_t += (Y[i] -  mean_y) ** 2
            ss_r += (Y[i] - y_pred) **2

        r2 = 1 - (ss_r/ss_t)

        print(r2)


def main():
    print("-----Linear Regression On Head and Brain Size data set-----")

    HeadBrainPredictor("HeadBrain.xlsx")

if __name__ == "__main__":
    main()