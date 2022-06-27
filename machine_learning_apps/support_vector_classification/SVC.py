import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from tkinter import (
    END,
    Button,
    Entry,
    Label,
    StringVar,
    Tk,
    mainloop,
    messagebox)
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

dataset = pd.read_csv('C:\\Users\\user\\python\\python_apps\\advanced_level_python_apps\\machine_learning_apps\\datasets\\Buy_Book.csv')

for column in dataset.columns:
    if dataset[column].dtype == type(object):
        le = LabelEncoder()
        dataset[column] = le.fit_transform(dataset[column])

X = dataset.iloc[0:, 0:4].values
Y = dataset.iloc[0:, -1].values

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.4, random_state=0)

classifier = SVC()   # tht datasets it is not good this is just an example
classifier.fit(X_train, Y_train)


def model_pred():
    try:
        age1 = entry1.get()
        age = int(age1)

        student1 = entry2.get()
        student = int(student1)

        income1 = entry3.get()
        income = int(income1)

        savings1 = entry4.get()
        savings = int(savings1)

        tran_variables = np.array([[age, student, income, savings]])
        pred_buy1 = classifier.predict(tran_variables)
        if str(pred_buy1) == '[1]':
            pred_price.set('The person will buy the book!')
        else:
            pred_price.set('The person will not buy the book!')
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
    entry4.delete(0, END)


window = Tk()
window.geometry('600x400')
window.title('Template Window')
# Age
label1 = Label(
    window, text='Enter the Age of the person',
    fg='red', font=('Courier', 15))
label1.pack()

age = StringVar()
age.set('')

entry1 = Entry(
    window, textvariable=age, fg='green', width=10, font=('Courier', 15))
entry1.pack()
# Student
label2 = Label(
    window, text='Student: (0 if not, 1 if yes)',
    fg='red', font=('Courier', 15))
label2.pack()

student = StringVar()
student.set('')

entry2 = Entry(
    window, textvariable=student, fg='green', width=10, font=('Courier', 15))
entry2.pack()
# Income
label3 = Label(
    window, text='Level of Income: (0 if high, 1 if low, 2 if median)',
    fg='red', font=('Courier', 15))
label3.pack()

income = StringVar()
income.set('')

entry3 = Entry(
    window, textvariable=income, fg='green', width=10, font=('Courier', 15))
entry3.pack()
# Savings
label4 = Label(
    window, text='Have Savings: (0 if excellent, 1 if fair)',
    fg='red', font=('Courier', 15))
label4.pack()

savings = StringVar()
savings.set('')

entry4 = Entry(
    window, textvariable=savings, fg='green', width=10, font=('Courier', 15))
entry4.pack()

pred_button = Button(
    window, text='Predict', fg='red', command=model_pred, height=2, width=15)
pred_button.pack()

pred_price = StringVar()
pred_price.set('')

label1 = Label(
    window, textvariable=pred_price, fg='red', font=('Courier', 25))
label1.pack()

mainloop()
