from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures

def readFile():
    dataset = pd.read_csv('C:\\Users\\user\\python\\python_apps\\advanced_level_python_apps\\machine_learning_apps\\datasets\\Nova pasta\\baseballplayer.csv')
    X = dataset.iloc[0:, 0].values
    Y = dataset.iloc[0:, -1].values
    return X, Y


def model_train(X, Y):

    X1 = np.reshape(X, (-1, 1))
    Y1 = np.reshape(Y, (-1, 1))
    
    poly_reg = PolynomialFeatures(degree=2)
    
    tran_X = poly_reg.fit_transform(X1)
    
    regressor = LinearRegression()
    regressor.fit(tran_X, Y1)
    
    return regressor


def visualize_results(X1, Y1, regressor, tran_X):

    plt.scatter(X1, Y1, color='red')
    plt.plot(X1, regressor.predict(tran_X), color='blue')
    plt.title('Angle vs Distance')
    plt.xlabel('Angle wich the ball is hitted')
    plt.title('Distance covered by the ball')

    plt.show()

def main():
    X, Y = readFile()
    classifier = model_train(X, Y)
    visualize_results(classifier)

