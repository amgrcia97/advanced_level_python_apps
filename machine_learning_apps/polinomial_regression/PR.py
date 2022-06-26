import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from tkinter import (
    END,
    Button,
    Entry,
    Label,
    StringVar,
    Tk,
    mainloop,
    messagebox)

dataset = pd.read_csv('C:\\Users\\user\\python\\python_apps\\advanced_level_python_apps\\machine_learning_apps\\datasets\\Nova pasta\\baseballplayer.csv')

X = dataset.iloc[0:, 0].values
Y = dataset.iloc[0:, -1].values

X1 = np.reshape(X, (-1, 1))
Y1 = np.reshape(Y, (-1, 1))

poly_reg = PolynomialFeatures(degree=2)

tran_X = poly_reg.fit_transform(X1)

regressor = LinearRegression()
regressor.fit(tran_X, Y1)


def model_pred():
    try:
        angle1 = entry.get()
        angle = int(angle1)

        tran_area = np.array([[angle]])
        tran_X = poly_reg.fit_transform(tran_area)
        pred_distance1 = regressor.predict(tran_X)
        pred_distance.set('Distance covered by the ball: \n' + str(pred_distance1)[2:8] + ' metters.')
    except Exception as e:
        print(e)
        messagebox.showerror(
                'Incorrect Data',
                message=(
                    'Please provide correct information'))
        pred_distance1 = ''
        pred_distance.set(pred_distance1)
    entry.delete(0, END)


window = Tk()
window.geometry('600x200')
window.title('Template Window')

label = Label(
    window, text='Enter the Angle wich the ball is hitted',
    fg='red', font=('Courier', 15))
label.pack()

angle = StringVar()
angle.set('')

entry = Entry(
    window, textvariable=angle, fg='green', width=10, font=('Courier', 15))
entry.pack()

pred_button = Button(
    window, text='Predict', fg='red', command=model_pred, height=2, width=15)
pred_button.pack()

pred_distance = StringVar()
pred_distance.set('')

label1 = Label(
    window, textvariable=pred_distance, fg='red', font=('Courier', 20))
label1.pack()

mainloop()
