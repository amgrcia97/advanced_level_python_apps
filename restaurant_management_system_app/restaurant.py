from tkinter import (
    LEFT,
    RIGHT,
    SUNKEN,
    TOP,
    W,
    Entry,
    Frame,
    Label,
    StringVar,
    Tk
)
import random
import time


root = Tk()
root. geometry('1200x600+0+0')
root.title('Restaurant Management System')

Tops = Frame(root, bg='black', width=1200, height=400, relief=SUNKEN)
Tops.pack(side=TOP)

frame_1 = Frame(root, width=900, height=600, relief=SUNKEN)
frame_1.pack(side=LEFT)

frame_2 = Frame(root, width=400, height=600, relief=SUNKEN)
frame_2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

label_info = Label(
    Tops,
    font=('aria', 30, 'bold'),
    text='Restaurant Management System',
    fg='blue',
    bd=10,
    anchor=W)
label_info.grid(row=0, column=0)
label_info = Label(
    Tops,
    font=('aria', 30, 'bold'),
    text=localtime,
    fg='red',
    anchor=W)
label_info.grid(row=1, column=0)

text_input = StringVar()
operator = ''

txt_display = Entry(
    frame_2,
    font=('arial',
    20, 'bold'),
    textvariable=text_input,
    bd=5,
    insertwidth=7,
    bg='green',
    justify='right')
txt_display.grid(columnspan=4)

but_row = 1
but_column = 0

buttons = ['7', '8', '9', '+',
           '4', '5', '6', '-',
           '1', '2', '3', '*',
           '0', 'C', '.', '/',
           '=']

root.mainloop()
