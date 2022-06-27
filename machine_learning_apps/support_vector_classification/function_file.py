import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix


def readFile():
    dataset = pd.read_csv('C:\\Users\\user\\python\\python_apps\\advanced_level_python_apps\\machine_learning_apps\\datasets\\Buy_Book.csv')
    
    for column in dataset.columns:
        if dataset[column].dtype == type(object):
            le = LabelEncoder()
            dataset[column] = le.fit_transform(dataset[column])
    
    X = dataset.iloc[0:, 0:4].values
    Y = dataset.iloc[0:, -1].values
    return X, Y


def split_data(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.6, random_state=0)
    return X_train, X_test, Y_train, Y_test


def model_train(X_train, Y_train, X_test,  Y_test):
    
    classifier = SVC()
    classifier.fit(X_train, Y_train)

    y_pred = classifier.predict(X_test)

    accuracy = accuracy_score(Y_test, y_pred)
    
    cm = confusion_matrix(Y_test, y_pred)
    
    tran_age = np.array([[59,1, 0,0]])
    
    buy_book = classifier.predict(tran_age)

    return classifier


def visualize_results(X_train1, Y_train1, X_test1,  Y_test1, lin_regressor):

    plt.scatter(X_test1, Y_test1, color='blue')
    # plt.plot(X_test1, y_pred, color='red')
    plt.title('Area vs Price of the Land')
    plt.xlabel('Area of the Land in thousand Square Foot')
    plt.title('Price of the Land in Million USD')

    plt.show()
