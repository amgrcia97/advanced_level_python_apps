import tkinter
import socket
from tkinter import *
from threading import Thread


def receive():
    while True:
        try:
            msg = s.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except:
            print("There is an Error Receiving the Message")

def send():
    msg = my_msg.get()
    my_msg.set("")
    s.send(bytes(msg, "utf8"))
    if msg == "#quit":
        s.close()
        window.destroy()

def on_clossing():
    my_msg.set("#quit")
    send()

window = Tk()
window.title("Chat Room Application")
window.configure(bg="lightblue")


message_frame = Frame(window, height=100, width=100, bg="black")
message_frame.pack()

my_msg = StringVar()
my_msg.set("")

scrollbar = Scrollbar(message_frame)

msg_list = Listbox(message_frame, height=15, width=100, bg="grey", yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

label = Label(window, text="Enter the Message", fg="blue", font="NORMAL", bg="white")
label.pack()

entry_field =  Entry(window, textvariable=my_msg, fg="black", width=40)
entry_field.pack()

send_Button = Button(window, text="Send", font="NORMAL", fg="black", command=send)
send_Button.pack()

quit_Button = Button(window, text="Quit", font="NORMAL", fg="black", command=on_clossing)
quit_Button.pack()

Host = '127.0.0.1'
Port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))

receive_Thread = Thread(target=receive)
receive_Thread.start()

mainloop()
