from tkinter import (
    Button,
    PhotoImage,
    Tk,
    Label)
from pygame import mixer


window = Tk()


mixer.init()

window.geometry('300x300')
window.title('Pyhton Music Player')

text_label = Label(window, text='This is a Play Button')
text_label.pack()


def play_music():
    mixer.music.load('music_player_app/burn.mp3')
    mixer.music.play()


def stop_music():
    mixer.music.stop()


play_photo = PhotoImage(
    file='music_player_app/play2.png',
    height=150,
    width=150)
play_button = Button(window, image=play_photo, command=play_music)
play_button.pack()

stop_photo = PhotoImage(
    file='music_player_app/stop.png',
    height=150,
    width=150)
stop_button = Button(window, image=stop_photo, command=stop_music)
stop_button.pack()


window.mainloop()
