from tkinter import *
import smtplib
import re
from turtle import width


def login():
    if validate_login():
        global username
        global password
        username = str(entry_1.get())
        password = str(entry_2.get())
        global server
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        f_2.pack()
        btn_2.grid()
        label_4['text'] = 'Logged in!'
        root.after(10, root.grid)
        f_1.pack_forget()
        root.after(10, root.grid)
        f_3.pack()
        label_9.grid_remove()
        root.after(10, root.grid)


def hide_login_label():
    f_2.pack_forget()
    f_3.pack_forget()
    root.after(10, root.grid)


def send_mail():
    if validate_message():
        label_9.grid_remove()
        root.after(10, root.grid)
        reciever = str(entry_3.get())
        subject = str(entry_4.get())
        msg_body = str(entry_5.get())
        msg = 'From: ' + username + '\n' + 'To: ' + reciever + '\n' + 'Subject: ' + subject + '\n' + msg_body
        try:
            server.sendmail(username, reciever, msg)
            label_9.grid()
            label_9['text'] = 'Mail Sent!'
            root.after(10, label_9.grid)
        except Exception as e:
            label_9.grid()
            label_9['text'] = 'Error in Sending your Email!'
            root.after(10, label_9.grid)


def logout():
    try:
        server.quit()
        f_3.pack_forget()
        f_2.pack()
        label_4.grid()
        label_4['text'] = 'Logged out succesfully!'
        btn_2.grid_remove()
        f_1.pack()
        entry_2.delete(0, END)
        root.after(10, root.grid)
    except Exception as e:
        label_4['text'] = 'Error in logout'


def validate_login():
    email_text = str(entry_1.get())
    pass_text = str(entry_2.get())
    if email_text == '' or pass_text == '':
        f_2.pack()
        label_4.grid()
        label_4['text'] = 'Fill in all the fields please.'
        btn_2.grid_remove()
        root.after(10, root.grid)
        return False
    else:
        EMAIL_REGEX = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
        if not EMAIL_REGEX.match(email_text):
            f_2.pack()
            label_4.grid()
            label_4['text'] = 'Enter a valid Email Address please.'
            btn_2.grid_remove()
            root.after(10, root.grid)
            return False
        else:
            return True


def validate_message():
    email_text = str(entry_3.get())
    sub_text = str(entry_4.get())
    msg_text = str(entry_5.get())

    if email_text == '' or sub_text == '' or msg_text == '':
        label_9.grid()
        label_9['text'] = 'Fill in all the fields please.'
        root.after(10, root.grid)
        return False
    else:
        EMAIL_REGEX = re.compile(r'[^@\s] + @[^@\s] + \.[a-zA-Z0-9] + $')
        if not EMAIL_REGEX.match(email_text):
            label_9.grid()
            label_9['text'] = 'Enter a valid email please.'
            root.after(10, root.grid)
            return False  
        elif len(sub_text) < 3 or len(msg_text) < 3:
            label_9.grid()
            label_9['text'] = 'Enter atleast e characters please.'
            root.after(10, root.grid)
            return False
        else:
            return True


root = Tk()
root.title('Email Application')

f_1 = Frame(root, width=1000, height=800)
f_1.pack(side=TOP)

label_1 = Label(f_1, width=25, text='Enter your Credentials', font=('Calibri 18 bold'))
label_1.grid(row=0, columnspan=3, pady=10, padx=10)

label_2 = Label(f_1, text='Email').grid(row=1, sticky=E, pady=5, padx=10)

label_3 = Label(f_1, text='Password').grid(row=2, sticky=E, pady=5, padx=10)

entry_1 = Entry(f_1)
entry_1.grid(row=1, column=1, pady=5)

entry_2 = Entry(f_1, show='*')
entry_2.grid(row=2, column=1)

btn_1 = Button(f_1, text='Login', width=10, bg='black', fg='white', command=lambda:login())
btn_1.grid(row=3, columnspan=3, pady=10)

f_2 = Frame(root)
f_2.pack(side=TOP, expand=NO, fill=NONE)

label_4 = Label(f_2, width=20, bg='cyan', fg='red', text='Log in Success', font=('Calibri 18 bold'))
label_4.grid(row=0, column=0, columnspan=2, pady=5)


btn_2 =  Button(f_2, text='Logout', bg='black', fg='white', command=lambda:logout())
btn_2.grid(row=0, column=4, sticky=E, pady=10, padx=(5, 0))

f_3 = Frame(master=root)
f_3.pack(side=TOP, expand=NO, fill=NONE)

label_5 = Label(f_3, width=20, text='Compose Email', font=('Calibri 18 bold'))
label_5.grid(row=0, columnspan=3, pady=10)

label_6 = Label(f_3, text='To').grid(row=1, sticky=E, pady=5)
label_7 = Label(f_3, text='Sibject').grid(row=2, sticky=E, pady=5)
label_8 = Label(f_3, text='Message').grid(row=3, sticky=E)

entry_3 = Entry(f_3)
entry_3.grid(row=1, column=1, pady=5)

entry_4 = Entry(f_3)
entry_4.grid(row=2, column=1, pady=5)

entry_5 = Entry(f_3)
entry_5.grid(row=3, column=1, pady=5, rowspan=3, ipady=10)

btn_3 = Button(f_3, text='Send Mail', width=10, bg='black', fg='white', command=lambda:send_mail())
btn_3.grid(row=6, columnspan=3, pady=10)

label_9 = Label(f_3, width=20, fg='white', bg='black', font=('Calibri 18 bold'))
label_9.grid(row=7, columnspan=3, pady=5)

hide_login_label()

root.mainloop()