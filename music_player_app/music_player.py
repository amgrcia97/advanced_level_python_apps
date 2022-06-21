from tkinter import (
    BOTTOM,
    SUNKEN,
    W,
    X,
    Frame,
    filedialog,
    HORIZONTAL,
    Button,
    Menu,
    PhotoImage,
    Scale,
    Tk,
    Label)
from pygame import mixer
import tkinter.messagebox


window = Tk()


mixer.init()

window.geometry('500x500')
window.title('Pyhton Music Player')


def browse_file():
    global file_name
    file_name = filedialog.askopenfilename()
    mixer.music.load(file_name)
    mixer.music.play()


def help_me():
    tkinter.messagebox.showinfo('Help', 'Some information about the app')


menu_bar = Menu(window)

sub_menu_1 = Menu(menu_bar, tearoff=0)
sub_menu_2 = Menu(menu_bar, tearoff=0)

window.config(menu=menu_bar)

menu_bar.add_cascade(label='File', menu=sub_menu_1)
sub_menu_1.add_command(label='Open', command=browse_file)
sub_menu_1.add_command(label='Exit', command=window.destroy)

menu_bar.add_cascade(label='About Us', menu=sub_menu_2)
sub_menu_2.add_command(label='Help', command=help_me)


text_label = Label(window, text='Pyhton Music Player')
text_label.pack()


def play_music():
    try:
        paused
    except Exception as e:
        print(e)
        try:
            mixer.music.load(file_name)
            mixer.music.play()
            status_bar['text'] = 'Music is playing'
        except Exception as e:
            print(e)
            tkinter.messagebox.showerror(
                'File Not Found',
                message="Please select a file")
            browse_file()
    if status_bar['text'] == 'Music is stoped':
        tkinter.messagebox.showerror(
                'File Not Found',
                message="Please select a file")
        browse_file()
        status_bar['text'] = 'Music is playing'
    else:
        mixer.music.unpause()
        status_bar['text'] = 'Music is unpaused'


def stop_music():
    mixer.music.stop()
    status_bar['text'] = 'Music is stoped'


def set_volume(value):
    volume = int(value)
    mixer.music.set_volume(volume)


def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    status_bar['text'] = 'Music is paused'


def rewind_music():
    mixer.music.rewind()
    status_bar['text'] = 'Music is rewinded'


frame = Frame(window)
frame.pack(pady=10, padx=10)


play_photo = PhotoImage(
    file='music_player_app/play2.png',
    height=100,
    width=100)
play_button = Button(frame, image=play_photo, command=play_music)
play_button.grid(row=0, column=0, padx=10)

stop_photo = PhotoImage(
    file='music_player_app/stop.png',
    height=100,
    width=100)
stop_button = Button(frame, image=stop_photo, command=stop_music)
stop_button.grid(row=0, column=1, padx=10)

pause_photo = PhotoImage(
    file='music_player_app/pause.png',
    height=100,
    width=100)
pause_button = Button(frame, image=pause_photo, command=pause_music)
pause_button.grid(row=0, column=2, padx=10)


frame_1 = Frame(window)
frame_1.pack()

rewind_photo = PhotoImage(
    file='music_player_app/rewind.png',
    height=50,
    width=100)
rewind_button = Button(frame_1, image=rewind_photo, command=rewind_music)
rewind_button.grid(row=0, column=0)

scale = Scale(frame_1, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70)
scale.grid(row=0, column=1)

status_bar = Label(
    window,
    text='Keep enjoying the music',
    relief=SUNKEN,
    anchor=W)
status_bar.pack(side=BOTTOM, fill=X)


window.mainloop()
