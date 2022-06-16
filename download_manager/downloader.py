from pytube import YouTube
from tkinter import filedialog, ttk
from tkinter import *
import re
import threading


class Application:

    def __init__(self, root):
        self.root = root
        self.root.grid_rowconfigure(0, weight=2)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(bg='#ffdddd')

        top_label = Label(self.root, text='YouTube Download Manager', fg='orange', font=('Type Xero', 70))
        top_label.grid(pady=(0, 10))

        link_label = Label(self.root, text='Please Paste Any Youtube Video Link Below', font=('SnowPersons', 30))
        link_label.grid(pady=(0, 20))

        self.youtube_entry_var = StringVar()

        self.youtube_entry = Entry(self.root, width=70, textvariable=self.youtube_entry_var, font=('Agency Fb', 25), fg='black')
        self.youtube_entry.grid(pady=(0, 15), ipady=2)

        self.youtube_entry_error = Label(self.root, text='', font=('Concert One', 20))
        self.youtube_entry_error.grid(pady=(0, 8))

        self.youtube_file_save_label = Label(self.root, text='Chose Directory', font=('Concert One', 30))
        self.youtube_file_save_label.grid()

        self.youtube_file_directory_button =  Button(self.root, text='Directory', font=('Bell MT', 15), command=self.open_directory)
        self.youtube_file_directory_button.grid(pady=(10,3))

        self.file_location_label = Label(self.root, text='', font=('Freestyle Script', 25))
        self.file_location_label.grid()
    
    def open_directory(self):
        self.folder_name = filedialog.askdirectory()
        if len(self.folder_name) > 0:
            self.file_location_label.config(text=self.folder_name, fg='green')
            return True
        else:
            self.file_location_label.config(text='Please Choose a Directory', fg='red')


if __name__ == '__main__':

    window = Tk()
    window.title('YouTube Download Manager')
    window.state('zoomed')

    app = Application(window)

    mainloop()