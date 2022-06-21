from tkinter import (
    HORIZONTAL,
    Button,
    Menu,
    PhotoImage,
    Scale,
    Tk,
    Label)
from pygame import mixer


window = Tk()


mixer.init()

window.geometry('300x300')
window.title('Pyhton Music Player')


menu_bar = Menu(window)

sub_menu_1 = Menu(menu_bar, tearoff=0)
sub_menu_2 = Menu(menu_bar, tearoff=0)

window.config(menu=menu_bar)

menu_bar.add_cascade(label='Fire', menu=sub_menu_1)
sub_menu_1.add_command(label='Open')
sub_menu_1.add_command(label='Exit')

menu_bar.add_cascade(label='About Us', menu=sub_menu_2)
sub_menu_2.add_command(label='Help')


text_label = Label(window, text='This is a Play Button')
text_label.pack()


def play_music():
    mixer.music.load('music_player_app/burn.mp3')
    mixer.music.play()


def stop_music():
    mixer.music.stop()


def set_volume(value):
    volume = int(value)
    mixer.music.set_volume(volume)


play_photo = PhotoImage(
    file='music_player_app/play2.png',
    height=100,
    width=100)
play_button = Button(window, image=play_photo, command=play_music)
play_button.pack()

stop_photo = PhotoImage(
    file='music_player_app/stop.png',
    height=100,
    width=100)
stop_button = Button(window, image=stop_photo, command=stop_music)
stop_button.pack()

scale = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70)
scale.pack()


window.mainloop()
