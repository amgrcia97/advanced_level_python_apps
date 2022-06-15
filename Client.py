import tkinter
import socket
from tkinter import (
    BOTH,
    LEFT,
    RIGHT,
    Y,
    Tk,
    Frame,
    StringVar,
    Scrollbar,
    Listbox,
    mainloop,
)
from threading import Thread


window = Tk()
window.title("Chat Room Application")
window.configure(bg="green")


message_frame = Frame(window, height=100, width=100, bg="red")
message_frame.pack()

my_msg = StringVar()
my_msg.set("")

scrollbar = Scrollbar(message_frame)

msg_list = Listbox(message_frame, height=15, width=100, bg='red', yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

mainloop()
