from tkinter import (
    LEFT,
    Button,
    DoubleVar,
    Entry,
    Label,
    StringVar,
    Tk,
    messagebox)


root = Tk()
root.title('BMI Calculator')
root.configure(width=100, height=100)
root.configure(bg='black')


height = StringVar()
height_label = Label(
    root, text='Height (m)', fg='red', bg='black',
    font=('Calibri 14 bold'), padx=5, pady=5)
height_label.grid(row=2)

height_entry = Entry(root, textvariable=height)
height_entry.grid(row=2, column=1, columnspan=2, padx=5)

mass = StringVar()
mass_label = Label(
    root, text='Mass (kg)', fg='red', bg='black',
    font=('Calibri 14 bold'), padx=10, pady=2)
mass_label.grid(row=4)

mass_entry = Entry(root, textvariable=mass)
mass_entry.grid(row=4, column=1, columnspan=2, padx=5)

bmi_val = DoubleVar()
stat_val = StringVar()

bmi_label = Label(
    root, text='BMI: ', fg='blue', bg='black',
    font=('Calibri 14 bold'), padx=2, pady=10,
    justify=LEFT)
bmi_label.grid(row=6)

bmi_total = Label(
    root, textvariable=bmi_val, fg='white', bg='black',
    font=('Calibri 14 bold'), padx=2, pady=10,
    justify=LEFT)
bmi_total.grid(row=6, column=1)

stat_label = Label(
    root, text='Status', fg='blue', bg='black',
    font=('Calibri 14 bold'), padx=2, pady=10,
    justify=LEFT)
stat_label.grid(row=7)

stat_msg = Label(
    root, textvariable=stat_val, fg='white', bg='black',
    font=('Calibri 14 bold'), padx=2, pady=10,
    justify=LEFT)
stat_msg.grid(row=7, column=1)

bmi_val.set('Mass / (Height ** 2)')
stat_val.set('')
height.set('')
mass.set('')

exp_mass = StringVar()
exp_mass.set('')

exp_mass_label = Label(
    root, text='Ideal Mass', fg='blue', bg='black',
    font=('Calibri 14 bold'), padx=2, pady=10,
    justify=LEFT)
exp_mass_label.grid(row=8)
exp_mass_msg = Label(
    root, textvariable=exp_mass, fg='white', bg='black',
    font=('Calibri 14 bold'), padx=2, pady=10,
    justify=LEFT)
exp_mass_msg.grid(row=8, column=1)


def calc():
    try:
        if float(mass.get()) == 0 and float(height.get()) == 0:
            return messagebox.showerror(
                    'Incorrect Data',
                    message=(
                        'Plase inform a valid Heiht and Mass: \n'
                        + 'Heiht: "XXX.XX" m\n'
                        + 'Mass: "XXX.XX" Kg'))
        if float(mass.get()) == 0:
            return messagebox.showerror(
                    'Incorrect Data',
                    message=(
                        'Plase inform a valid Mass: "XXX.XX Kg"'))
        if float(height.get()) == 0:
            return messagebox.showerror(
                    'Incorrect Data',
                    message=(
                        'Plase inform a valid Heiht: "XXX.XX m"'))
        bmi = float(float(mass.get()) / (float(height.get())) ** 2)
        Stat = getStatus(bmi)
        stat_val.set(Stat)
        h = float(height.get())
        Ideal = getIdealMass(h)
        exp_mass.set(Ideal)
        bmi_val.set(format(bmi, '.2f'))

    except Exception:
        messagebox.showerror(
                'Incorrect Data',
                message=(
                    'Plase inform a valid Heiht and Mass: \n'
                    + 'Heiht: "XXX.XX" m\n'
                    + 'Mass: "XXX.XX" Kg'))


def clear():
    bmi_val.set('Mass / (Height ** 2)')
    stat_val.set('')
    height.set('')
    mass.set('')
    exp_mass.set('')


def getStatus(bmi):
    if bmi > 40:
        return 'You are Obess Class 3'
    elif 40 > bmi > 35:
        return 'You are Obess Class 2'
    elif 35 > bmi > 30:
        return 'You are Obess Class 1'
    elif 30 > bmi > 25:
        return 'You are OverWeight'
    elif 25 > bmi > 18.5:
        return 'You are Normal'
    elif 18.5 > bmi > 17:
        return 'You are Mild Thin'
    else:
        return 'You are Moderately Thin'


def getIdealMass(height):
    max_mass = 25 * (height ** 2)
    min_mass = 18.5 * (height ** 2)
    return str('%.2f' % (max_mass)) + ' To ' + str('%.2f' % (min_mass)) + 'Kg.'


calculate = Button(
    root, text='Calculate', command=calc, fg='black', bg='white',
    font=('Calibri 14 bold'))
calculate.grid(row=9)

clear = Button(
    root, text='Reset', command=clear, fg='black', bg='white',
    font=('Calibri 14 bold'))
clear.grid(row=9, column=3)

root.mainloop()
