import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression
from tkinter import (
    END,
    Button,
    Entry,
    Label,
    StringVar,
    Tk,
    mainloop,
    messagebox)

dataset = pd.read_csv('C:\\Users\\user\\python\\python_apps\\advanced_level_python_apps\\machine_learning_apps\\datasets\\landprice1.csv')

X = dataset.iloc[0:, 0].values
Y = dataset.iloc[0:, -1].values

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.4, random_state=0)

X_train1 = np.reshape(X_train, (-1, 1))
Y_train1 = np.reshape(Y_train, (-1, 1))

X_test1 = np.reshape(X_test, (-1, 1))
Y_test1 = np.reshape(Y_test, (-1, 1))

lin_regressor = LinearRegression()
lin_regressor.fit(X_train1, Y_train1)


def model_pred():
    try:
        area1 = entry.get()
        area = int(area1)

        tran_area = np.array([[area]])
        pred_price1 = lin_regressor.predict(tran_area)
        pred_price.set('USD ' + str(pred_price1)[2:6] + ' millions')
    except Exception:
        messagebox.showerror(
                'Incorrect Data',
                message=(
                    'Please provide correct information'))
        pred_price1 = ''
        pred_price.set(pred_price1)
    entry.delete(0, END)


window = Tk()
window.geometry('600x200')
window.title('Template Window')

label = Label(
    window, text='Enter the Area of the land in thousadn Sq Foot',
    fg='red', font=('Courier', 15))
label.pack()

area = StringVar()
area.set('')

entry = Entry(
    window, textvariable=area, fg='green', width=10, font=('Courier', 15))
entry.pack()

pred_button = Button(
    window, text='Predict', fg='red', command=model_pred, height=2, width=15)
pred_button.pack()

pred_price = StringVar()
pred_price.set('')

label1 = Label(
    window, textvariable=pred_price, fg='red', font=('Courier', 25))
label1.pack()

mainloop()
