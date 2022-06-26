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

dataset = pd.read_csv('C:\\Users\\user\\python\\python_apps\\advanced_level_python_apps\\simple_linear_regression\\datasets\\landprice1.csv')

X = dataset.iloc[0:, 0:3].values
Y = dataset.iloc[0:, -1].values

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.4, random_state=0)

lin_regressor = LinearRegression()
lin_regressor.fit(X_train, Y_train)


def model_pred():
    try:
        area1 = entry1.get()
        area = int(area1)

        distance1 = entry2.get()
        distance = int(distance1)

        crime1 = entry3.get()
        crime = int(crime1)

        tran_variables = np.array([[area, distance, crime]])
        pred_price1 = lin_regressor.predict(tran_variables)
        print(pred_price1)
        pred_price.set('USD ' + str(pred_price1)[1:6] + ' millions')
    except Exception:
        messagebox.showerror(
                'Incorrect Data',
                message=(
                    'Please provide correct information'))
        pred_price1 = ''
        pred_price.set(pred_price1)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)


window = Tk()
window.geometry('600x400')
window.title('Template Window')
# Area
label1 = Label(
    window, text='Enter the Area of the land in thousadn Sq Foot',
    fg='red', font=('Courier', 15))
label1.pack()

area = StringVar()
area.set('')

entry1 = Entry(
    window, textvariable=area, fg='green', width=10, font=('Courier', 15))
entry1.pack()
# Distance
label2 = Label(
    window, text='Enter the Distance From City Centre',
    fg='red', font=('Courier', 15))
label2.pack()

distance = StringVar()
distance.set('')

entry2 = Entry(
    window, textvariable=distance, fg='green', width=10, font=('Courier', 15))
entry2.pack()
# Crime rate
label3 = Label(
    window, text='Enter the Crime Rate in that Region',
    fg='red', font=('Courier', 15))
label3.pack()

crime = StringVar()
crime.set('')

entry3 = Entry(
    window, textvariable=crime, fg='green', width=10, font=('Courier', 15))
entry3.pack()

pred_button = Button(
    window, text='Predict', fg='red', command=model_pred, height=2, width=15)
pred_button.pack()

pred_price = StringVar()
pred_price.set('')

label1 = Label(
    window, textvariable=pred_price, fg='red', font=('Courier', 25))
label1.pack()

mainloop()
