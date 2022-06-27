import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix

def readFile():
    dataset = pd.read_csv('C:\\Users\\user\\python\\python_apps\\advanced_level_python_apps\\machine_learning_apps\\datasets\\Buy_Book1.csv')
    X = dataset.iloc[0:, 0].values
    Y = dataset.iloc[0:, -1].values
    return X, Y

def split_data(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.4, random_state=0)
    return X_train, X_test, Y_train, Y_test

def model_train(X_train, X_test, Y_train, Y_test):

    X_train1 = np.reshape(X_train, (-1, 1))
    Y_train1 = np.reshape(Y_train, (-1, 1))

    X_test1 = np.reshape(X_test, (-1, 1))
    Y_test1 = np.reshape(Y_test, (-1, 1))

    classifier = LogisticRegression()
    classifier.fit(X_train1, Y_train1)
    
    y_pred = classifier.predict(X_test1)
    
    accuracy = accuracy_score(Y_test1, y_pred)
    cm = confusion_matrix(Y_test1, y_pred)
    
    age = 44
    
    tran_age = np.array([[age]])
    
    pred_buybook = classifier.predict(tran_age)

    return classifier

def visualize_results(X, Y, regressor, tran_X):

    plt.scatter(X, Y, color='blue')
    # plt.plot(X1, regressor.predict(tran_X), color='blue')
    plt.title('Angle vs Buy Book')
    plt.xlabel('Age')
    plt.title('Buy Book')

    plt.show()

def main():
    X, Y = readFile()
    classifier = model_train(X, Y)
    visualize_results(classifier)

