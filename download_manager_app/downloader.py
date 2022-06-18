from pytube import YouTube
from tkinter import (
    Button,
    Entry,
    Radiobutton,
    StringVar,
    Tk,
    Toplevel,
    filedialog,
    mainloop,
    ttk,
    Label)
import re
import threading


class DownloaderApp:

    def __init__(self, root):
        self.root = root
        self.root.grid_rowconfigure(0, weight=2)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(bg='#ffdddd')

        top_label = Label(
            self.root,
            text='YouTube Download Manager',
            fg='orange',
            font=('Type Xero', 70))
        top_label.grid(pady=(0, 10))

        link_label = Label(
            self.root,
            text='Please Paste Any Youtube Video Link Below',
            font=('SnowPersons', 30))
        link_label.grid(pady=(0, 20))

        self.youtube_entry_var = StringVar()

        self.youtube_entry = Entry(
            self.root, width=70,
            textvariable=self.youtube_entry_var,
            font=('Agency Fb', 25),
            fg='black')
        self.youtube_entry.grid(pady=(0, 15), ipady=2)

        self.youtube_entry_error = Label(
            self.root, text='',
            font=('Concert One', 20))
        self.youtube_entry_error.grid(pady=(0, 8))

        self.youtube_file_save_label = Label(
            self.root,
            text='Chose Directory',
            font=('Concert One', 30))
        self.youtube_file_save_label.grid()

        self.youtube_file_directory_button = Button(
            self.root,
            text='Directory',
            font=('Bell MT', 15),
            command=self.open_directory)
        self.youtube_file_directory_button.grid(pady=(10, 3))

        self.file_location_label = Label(
            self.root, text='',
            font=('Freestyle Script', 25))
        self.file_location_label.grid()

        self.youtube_choose_label = Label(
            self.root, text='Choose the Download Type',
            font=('Variety', 30))
        self.youtube_choose_label.grid()

        self.download_choices = [('Audio MP3', 1), ('Video MP4', 2)]

        self.choices_var = StringVar()
        self.choices_var.set(1)

        for text, mode in self.download_choices:
            self.youtube_choices = Radiobutton(
                self.root,
                text=text,
                font=('NorthWest old', 15),
                variable=self.choices_var,
                value=mode)
            self.youtube_choices.grid()

        self.dowload_button = Button(
            self.root, text='Download',
            width=10,
            font=('Bell MT', 15),
            command=self.check_youtube_link)
        self.dowload_button.grid(pady=(30, 5))

    def check_youtube_link(self):
        self.match_youtube_link = re.match(
            '^https://www.youtube.com/.',
            self.youtube_entry_var.get())

        if not self.match_youtube_link:
            self.youtube_entry_error.config(
                text='Invalid Youtube Link',
                fg='red')

        elif not self.open_directory:
            self.file_location_label.config(
                text='Please Choose a valid Directory',
                fg='red')

        elif self.match_youtube_link and self.open_directory:
            self.download_window()

    def download_window(self):
        self.new_window = Toplevel(self.root)
        self.root.withdraw()

        self.new_window.state('zoomed')
        self.new_window.grid_rowconfigure(0, weight=0)
        self.new_window.grid_columnconfigure(0, weight=1)

        self.app = DowloadApp(
            self.new_window,
            self.youtube_entry_var.get(),
            self.folder_name,
            self.choices_var.get())

    def open_directory(self):
        self.folder_name = filedialog.askdirectory()
        if (len(self.folder_name) > 0):
            self.file_location_label.config(
                text=self.folder_name,
                fg='green')
            return True
        else:
            self.file_location_label.config(
                text='Please Choose a Directory',
                fg='red')


class DowloadApp:

    def __init__(self, download_window, youtube_link, folder_name, choices):
        self.download_window = download_window
        self.youtube_link = youtube_link
        self.folder_name = folder_name
        self.choices = choices

        self.yt = YouTube(self.youtube_link)

        if (choices == '1'):
            self.video_type = self.yt.streams.filter(only_audio=True).first()
            self.max_file_size = self.video_type.filesize
            print(self.max_file_size)

        elif (choices == '2'):
            self.video_type = self.yt.streams.first()
            self.max_file_size = self.video_type.filesize
            print(self.max_file_size)

        self.loading_label = Label(
            self.download_window,
            text='Dowloading in Progress...',
            font=('Small Fonts', 40))
        self.loading_label.grid(pady=(100, 0))

        self.loading_percent_label = Label(
            self.download_window,
            text='0',
            fg='green',
            font=('Agency Fb', 40))
        self.loading_percent_label.grid(pady=(50, 0))

        self.progress_bar = ttk.Progressbar(
            self.download_window,
            length=500,
            orient='horizontal',
            mode='indeterminate')
        self.progress_bar.grid(pady=(50, 0))
        self.progress_bar.start()

        threading.Thread(
            target=self.yt.register_on_progress_callback(
                self.on_progress)).start()

        threading.Thread(target=self.download_file).start()

    def download_file(self):
        if self.choices == '1':
            self.yt.streams.filter(
                only_audio=True).first().download(self.folder_name)

        if self.choices == '2':
            self.yt.streams.filter(
                progressive=True,
                file_extension='mp4').first().download(self.folder_name)

    def on_progress(self, stream=None, chunks=None, bytes_remaining=None):

        print('bytes_remaining: ', bytes_remaining)
        print('total: ', self.max_file_size)
        self.percent_count = float(
            "%0.2f" % (100-(((bytes_remaining*10)/self.max_file_size))))
        print('percent: ', self.percent_count)

        if (self.percent_count < 100.00):
            self.loading_percent_label.config(text=self.percent_count)
            print('downloading %')
        else:
            self.loading_percent_label.config(text='100.00 %')
            self.progress_bar.stop()
            self.loading_label.grid_forget()
            self.progress_bar.grid_forget()

            self.download_finished = Label(
                self.download_window,
                text='Download finished!',
                font=('Agency Fb', 30))
            self.download_finished.grid(pady=(150, 0))

            self.download_file_name = Label(
                self.download_window,
                text=self.yt.title,
                font=('Terminal', 30))
            self.download_file_name.grid(pady=(50, 0))

            MB = float('%0.2f' % (self.max_file_size/199399))

            self.download_file_size = Label(
                self.download_window,
                text=str(MB),
                font=('Agency Fb', 30))
            self.download_file_size.grid(pady=(50, 0))


if __name__ == '__main__':

    window = Tk()
    window.title('YouTube Download Manager')
    window.state('zoomed')

    app = DownloaderApp(window)

    mainloop()
