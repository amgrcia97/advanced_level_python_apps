from tkinter import (
    messagebox,
    LEFT,
    RIGHT,
    SUNKEN,
    TOP,
    W,
    Button,
    Entry,
    Frame,
    Label,
    StringVar,
    Tk
)
import random
import time


root = Tk()
root. geometry('1250x650+0+0')
root.title('Restaurant Management System')

Tops = Frame(root, width=1200, height=400, relief=SUNKEN)
Tops.pack(side=TOP)

frame_1 = Frame(root, width=875, height=525, relief=SUNKEN, )
frame_1.pack(side=LEFT)

frame_2 = Frame(root, width=400, height=525, relief=SUNKEN, bg='darkgray')
frame_2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

label_info = Label(
    Tops,
    font=('aria', 20, 'bold'),
    text='Restaurant Management System',
    fg='black',
    bd=10,
    anchor=W)
label_info.grid(row=0, column=0)
label_info = Label(
    Tops,
    font=('aria', 20, 'bold'),
    text='          ',
    bd=10,
    fg='black',
    anchor=W
    )
label_info.grid(row=0, column=1)
label_info = Label(
    Tops,
    font=('aria', 20, 'bold'),
    text=localtime,
    bd=10,
    fg='black',
    anchor=W
    )
label_info.grid(row=0, column=2)

text_input = StringVar()
operator = ''

txt_display = Entry(
    frame_2,
    font=('arial', 20, 'bold'),
    textvariable=text_input,
    bd=5,
    insertwidth=7,
    bg='green',
    justify='right')
txt_display.grid(columnspan=4)


def button_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def clrdisplay():
    global operator
    operator = ''
    text_input.set('')


def equals():
    global operator
    try:
        sumup = str(eval(operator))
        text_input.set(sumup)
        operator = ''
    except Exception as e:
        error = str(e)
        text_input.set(error[0:14])
        operator = ''


button_7 = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='7', bg='black', command=lambda: button_click(7))
button_7.grid(row=2, column=0)
button_8 = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='8', bg='black', command=lambda: button_click(8))
button_8.grid(row=2, column=1)
button_9 = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='9', bg='black', command=lambda: button_click(9))
button_9.grid(row=2, column=2)
button_add = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='+', bg='black', command=lambda: button_click('+'))
button_add.grid(row=2, column=3)

button_4 = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='4', bg='black', command=lambda: button_click(4))
button_4.grid(row=3, column=0)
button_5 = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='5', bg='black', command=lambda: button_click(5))
button_5.grid(row=3, column=1)
button_6 = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='6', bg='black', command=lambda: button_click(6))
button_6.grid(row=3, column=2)
button_minus = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='-', bg='black', command=lambda: button_click('-'))
button_minus.grid(row=3, column=3)

button_1 = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='1', bg='black', command=lambda: button_click(1))
button_1.grid(row=4, column=0)
button_2 = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='2', bg='black', command=lambda: button_click(2))
button_2.grid(row=4, column=1)
button_3 = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='3', bg='black', command=lambda: button_click(3))
button_3.grid(row=4, column=2)
button_mult = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='*', bg='black', command=lambda: button_click('*'))
button_mult.grid(row=4, column=3)

button_0 = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='0', bg='black', command=lambda: button_click(0))
button_0.grid(row=5, column=0)
button_c = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='c', bg='black', command=clrdisplay)
button_c.grid(row=5, column=1)
button_dec = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='.', bg='black', command=lambda: button_click('.'))
button_dec.grid(row=5, column=2)
button_div = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='/', bg='black', command=lambda: button_click('/'))
button_div.grid(row=5, column=3)

button_eq = Button(
    frame_2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
    text='=', bg='black', width=15, command=equals)
button_eq.grid(row=6, columnspan=4)

Rand = StringVar()
x = random.randint(12000, 50000)
random_ref = str(x)
Rand.set(random_ref)

Fries = StringVar()
Fries.set(0)
LargeFries = StringVar()
LargeFries.set(0)
Burguer = StringVar()
Burguer.set(0)
Filet = StringVar()
Filet.set(0)
Cheese_Burguer = StringVar()
Cheese_Burguer.set(0)
Drinks = StringVar()
Drinks.set(0)
Subtotal = StringVar()
Subtotal.set('R$: 0')
Total = StringVar()
Total.set('R$: 0')
Service_Charge = StringVar()
Service_Charge.set('R$: 0')
Tax = StringVar()
Tax.set('0.33 %')
Cost = StringVar()
Cost.set('R$: 0')

label_ref = Label(
    frame_1, font=('arial', 15, 'bold'), text='Order No.', fg='black',
    bd=10, anchor=W)
label_ref.grid(row=0, column=0)
txt_reference = Entry(
    frame_1, font=('arial', 15, 'bold'), textvariable=Rand, bd=6,
    insertwidth=4, bg='red', justify='right')
txt_reference.grid(row=0, column=1)

label_fries = Label(
    frame_1, font=('arial', 15, 'bold'), text='Fries Meal', fg='black',
    bd=10, anchor=W)
label_fries.grid(row=1, column=0)
txt_fries = Entry(
    frame_1, font=('arial', 15, 'bold'), textvariable=Fries, bd=6,
    insertwidth=4, bg='red', justify='right')
txt_fries.grid(row=1, column=1)

label_LargeFries = Label(
    frame_1, font=('arial', 15, 'bold'), text='Lunch Meal', fg='black',
    bd=10, anchor=W)
label_LargeFries.grid(row=2, column=0)
txt_LargeFries = Entry(
    frame_1, font=('arial', 15, 'bold'), textvariable=LargeFries, bd=6,
    insertwidth=4, bg='red', justify='right')
txt_LargeFries.grid(row=2, column=1)

label_Burguer = Label(
    frame_1, font=('arial', 15, 'bold'), text='Burguer Meal', fg='black',
    bd=10, anchor=W)
label_Burguer.grid(row=3, column=0)
txt_Burguer = Entry(
    frame_1, font=('arial', 15, 'bold'), textvariable=Burguer, bd=6,
    insertwidth=4, bg='red', justify='right')
txt_Burguer.grid(row=3, column=1)

label_Filet = Label(
    frame_1, font=('arial', 15, 'bold'), text='Pizza Meal', fg='black',
    bd=10, anchor=W)
label_Filet.grid(row=4, column=0)
txt_Filet = Entry(
    frame_1, font=('arial', 15, 'bold'), textvariable=Filet, bd=6,
    insertwidth=4, bg='red', justify='right')
txt_Filet.grid(row=4, column=1)

label_Cheese_Burguer = Label(
    frame_1, font=('arial', 15, 'bold'), text='Cheese_Burguer Meal',
    fg='black', bd=10, anchor=W)
label_Cheese_Burguer.grid(row=5, column=0)
txt_Cheese_Burguer = Entry(
    frame_1, font=('arial', 15, 'bold'), textvariable=Cheese_Burguer, bd=6,
    insertwidth=4, bg='red', justify='right')
txt_Cheese_Burguer.grid(row=5, column=1)

label_Drinks = Label(
    frame_1, font=('arial', 15, 'bold'), text='Drinks', fg='black',
    bd=10, anchor=W)
label_Drinks.grid(row=0, column=2)
txt_Drinks = Entry(
    frame_1, font=('arial', 15, 'bold'), textvariable=Drinks, bd=6,
    insertwidth=4, bg='red', justify='right')
txt_Drinks.grid(row=0, column=3)

label_Subtotal = Label(
    frame_1, font=('arial', 15, 'bold'), text='Subtotal', fg='black',
    bd=10, anchor=W)
label_Subtotal.grid(row=1, column=2)
txt_Subtotal = Entry(
    frame_1, font=('arial', 15, 'bold'), textvariable=Subtotal, bd=6,
    insertwidth=4, bg='red', justify='right')
txt_Subtotal.grid(row=1, column=3)

label_Cost = Label(
    frame_1, font=('arial', 15, 'bold'), text='Cost', fg='black',
    bd=10, anchor=W)
label_Cost.grid(row=2, column=2)
txt_Cost = Entry(
    frame_1, font=('arial', 15, 'bold'), textvariable=Cost, bd=6,
    insertwidth=4, bg='red', justify='right')
txt_Cost.grid(row=2, column=3)

label_Service_Charge = Label(
    frame_1, font=('arial', 15, 'bold'), text='Service Charge', fg='black',
    bd=10, anchor=W)
label_Service_Charge.grid(row=3, column=2)
txt_Service_Charge = Entry(
    frame_1, font=('arial', 15, 'bold'), textvariable=Service_Charge, bd=6,
    insertwidth=4, bg='red', justify='right')
txt_Service_Charge.grid(row=3, column=3)

label_Tax = Label(
    frame_1, font=('arial', 15, 'bold'), text='Tax', fg='black',
    bd=10, anchor=W)
label_Tax.grid(row=4, column=2)
txt_Tax = Entry(
    frame_1, font=('arial', 15, 'bold'), textvariable=Tax, bd=6,
    insertwidth=4, bg='red', justify='right')
txt_Tax.grid(row=4, column=3)

label_Total = Label(
    frame_1, font=('arial', 15, 'bold'), text='Total', fg='black',
    bd=10, anchor=W)
label_Total.grid(row=5, column=2)
txt_Total = Entry(
    frame_1, font=('arial', 15, 'bold'), textvariable=Total, bd=6,
    insertwidth=4, bg='red', justify='right')
txt_Total.grid(row=5, column=3)


def reset():
    x = random.randint(12000, 50000)
    random_ref = str(x)
    Rand.set(random_ref)
    Fries.set(0)
    LargeFries.set(0)
    Burguer.set(0)
    Filet.set(0)
    Cheese_Burguer.set(0)
    Drinks.set(0)
    Subtotal.set('R$: 0')
    Total.set('R$: 0')
    Service_Charge.set('R$: 0')
    Tax.set('0.33 %')
    Cost.set('R$: 0')


def ref():
    try:
        fries = float(Fries.get())
    except Exception as e:
        e = 'Invalid'
        Fries.set(e)
        # fries = 0
    try:
        lunch_meal = float(LargeFries.get())
    except Exception as e:
        e = 'Invalid'
        LargeFries.set(e)
        # lunch_meal = 0
    try:
        burguer_meal = float(Burguer.get())
    except Exception as e:
        e = 'Invalid'
        Burguer.set(e)
        # burguer_meal = 0
    try:
        pizza_meal = float(Filet.get())
    except Exception as e:
        e = 'Invalid'
        Filet.set(e)
        # pizza_meal = 0
    try:
        cheesse_burguer = float(Cheese_Burguer.get())
    except Exception as e:
        e = 'Invalid'
        Cheese_Burguer.set(e)
        # cheesse_burguer = 0
    try:
        drinks = float(Drinks.get())
    except Exception as e:
        e = 'Invalid'
        Drinks.set(e)
        # drinks = 0

    meals = (
        Fries, LargeFries, Burguer, Filet, Cheese_Burguer, Drinks)

    for meal in meals:
        if meal.get() != 'Invalid':
            continue
        else:
            messagebox.showerror(
                'Incorrect Data',
                message=(
                    'Some field(s) is(are) incorrect(s) '
                    + 'please provide correct information'))
            return reset()

    fries_cost = fries * 25
    lunch_cost = lunch_meal * 40
    burguer_cost = burguer_meal * 35
    pizza_cost = pizza_meal * 50
    cheesse_burguer_cost = cheesse_burguer * 30
    drinks_cost = drinks * 35

    total_cost = (
        fries_cost + lunch_cost + burguer_cost + pizza_cost +
        cheesse_burguer_cost + drinks_cost)

    meal_cost = 'R$: ' + str('%.2f' % (total_cost))

    tax_payable = (total_cost * 0.33)

    service_charge = (total_cost / 99)

    service = 'R$: ' + str('%.2f' % (service_charge))

    overal_cost = 'R$: ' + str('%.2f' % (
        total_cost + tax_payable + service_charge))

    paid_tax = 'R$: ' + str('%.2f' % (tax_payable))

    Subtotal.set(meal_cost)
    Total.set(overal_cost)
    Service_Charge.set(service)
    Tax.set(paid_tax)
    Cost.set(meal_cost)


button_total = Button(
    frame_1, padx=16, pady=8, bd=10, fg='white', font=('arial', 16, 'bold'),
    width=10, text="TOTAL", bg='black', command=ref)
button_total.grid(row=7, column=0)


button_reset = Button(
    frame_1, padx=16, pady=8, bd=10, fg='white', font=('arial', 16, 'bold'),
    width=10, text="RESET", bg='black', command=reset)
button_reset.grid(row=7, column=1)


def qexit():
    root.destroy()


button_exit = Button(
    frame_1, padx=16, pady=8, bd=10, fg='white', font=('arial', 16, 'bold'),
    width=10, text="EXIT", bg='black', command=qexit)
button_exit.grid(row=7, column=2)


def price():
    roo = Tk()
    roo.geometry('600x220')
    roo.title('Price List')
    x = Frame(roo, width=600, height=220, relief=SUNKEN)
    x.pack(side=TOP)
    label_info = Label(
        x, font=('aria', 15, 'bold'), text='ITEM', fg='red', bd=5)
    label_info.grid(row=0, column=0)
    label_info = Label(
        x, font=('aria', 15, 'bold'), text='_____________', fg='black',
        anchor=W)
    label_info.grid(row=0, column=2)
    label_info = Label(
        x, font=('aria', 15, 'bold'), text='PRICE', fg='black', bd=5, anchor=W)
    label_info.grid(row=0, column=5)

    label_info = Label(
        x, font=('aria', 15, 'bold'), text='Fries Meal', fg='steel blue', bd=5,
        anchor=W)
    label_info.grid(row=1, column=0)
    label_info = Label(
        x, font=('aria', 15, 'bold'), text='25', fg='steel blue', bd=5,
        anchor=W)
    label_info.grid(row=1, column=5)

    label_info = Label(
        x, font=('aria', 15, 'bold'), text='Lunch Meal', fg='steel blue', bd=5,
        anchor=W)
    label_info.grid(row=2, column=0)
    label_info = Label(
        x, font=('aria', 15, 'bold'), text='40', fg='steel blue', bd=5,
        anchor=W)
    label_info.grid(row=2, column=5)

    label_info = Label(
        x, font=('aria', 15, 'bold'), text='Burguer Meal', fg='steel blue',
        bd=5, anchor=W)
    label_info.grid(row=3, column=0)
    label_info = Label(
        x, font=('aria', 15, 'bold'), text='35', fg='steel blue', bd=5,
        anchor=W)
    label_info.grid(row=3, column=5)

    label_info = Label(
        x, font=('aria', 15, 'bold'), text='Pizza Meal', fg='steel blue', bd=5,
        anchor=W)
    label_info.grid(row=4, column=0)
    label_info = Label(
        x, font=('aria', 15, 'bold'), text='50', fg='steel blue', bd=5,
        anchor=W)
    label_info.grid(row=4, column=5)

    label_info = Label(
        x, font=('aria', 15, 'bold'), text='Cheese Burguer', fg='steel blue',
        bd=5, anchor=W)
    label_info.grid(row=5, column=0)
    label_info = Label(
        x, font=('aria', 15, 'bold'), text='30', fg='steel blue', bd=5,
        anchor=W)
    label_info.grid(row=5, column=5)

    label_info = Label(
        x, font=('aria', 15, 'bold'), text='Drinks', fg='steel blue', bd=5,
        anchor=W)
    label_info.grid(row=6, column=0)
    label_info = Label(
        x, font=('aria', 15, 'bold'), text='35', fg='steel blue', bd=5,
        anchor=W)
    label_info.grid(row=6, column=5)

    x.pack()

    roo.mainloop()


button_price = Button(
    frame_1, padx=16, pady=8, bd=10, fg='white', font=('arial', 16, 'bold'),
    width=10, text="PRICE", bg='black', command=price)
button_price.grid(row=7, column=3)

root.mainloop()
