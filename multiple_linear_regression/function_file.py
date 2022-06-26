import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from tkinter import (
    Tk) 



def readFile():
    dataset = pd.read_csv('C:\\Users\\user\\python\\python_apps\\advanced_level_python_apps\\simple_linear_regression\\datasets\\landprice1.csv')
    
    X = dataset.iloc[0:, 0].values
    Y = dataset.iloc[0:, -1].values
    return X, Y

def split_data(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.4, random_state=0)
    return X_train, X_test, Y_train, Y_test


def model_train(X_train, Y_train, X_test,  Y_test):
    X_train1 = np.reshape(X_train, (-1, 1))
    Y_train1 = np.reshape(Y_train, (-1, 1))
    X_test1 = np.reshape(X_test, (-1, 1))
    Y_test1 = np.reshape(Y_test, (-1, 1))
    
    lin_regressor = LinearRegression()
    lin_regressor.fit(X_train1, Y_train1)

    return lin_regressor


def visualize_results(X_train1, Y_train1, X_test1,  Y_test1, lin_regressor):

    plt.scatter(X_test1, Y_test1, color='blue')
    plt.plot(X_test1, lin_regressor.predict(X_test1), color='red')
    plt.title('Area vs Price of the Land')
    plt.xlabel('Area of the Land in thousand Square Foot')
    plt.title('Price of the Land in Million USD')

    plt.show()

def main():
    X, Y = readFile()
    X_train, Y_train, X_test,  Y_test = split_data(X, Y)
    classifier = model_train(X_train, Y_train, X_test,  Y_test)
    visualize_results(X_train, Y_train, X_test,  Y_test, classifier)

