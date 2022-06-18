from tkinter import (
    E,
    W,
    Button,
    Checkbutton,
    Entry,
    IntVar,
    Label,
    Frame,
    Tk)
from tkinter import filedialog
import PyPDF2
import pyttsx3


def extract_text():
    file = filedialog.askopenfile(
        parent=root,
        mode='rb',
        title='Choose a PDF File')

    if file is not None:
        pdf_reader_obj = PyPDF2.PdfFileReader(file)
        global text_extracted
        text_extracted = ''
        for pageNum in range(pdf_reader_obj.numPages):
            page_obj = pdf_reader_obj.getPage(pageNum)
            text_extracted += page_obj.extractText()
        file.close()


def speak_text():
    global rate
    rate = int(rate.get())
    engine.setProperty('rate', rate)

    global male
    male = int(male.get())

    global female
    female = int(female.get())

    all_voices = engine.getProperty('voices')
    male_voice = all_voices[0].id
    female_voice = all_voices[1].id

    if male == 0 and female == 0 or male == 1 and female == 1:
        engine.setProperty('voice', male_voice)
    elif male == 0 and female == 1:
        engine.setProperty('voice', female_voice)
    else:
        engine.setProperty('voice', male_voice)

    engine.say(text_extracted)
    # engine.save_to_file(text_extracted, 'speech.mp3')
    engine.runAndWait()


def stop_speaking():
    engine.stop()


def Application(root):
    root.geometry('{}x{}'.format(700, 600))
    root.resizable(width=False, height=False)
    root.title('PDF to AUDIO')
    root.configure(background='light grey')
    global rate, male, female
    # frame1
    frame_1 = Frame(root, width=500, height=200, bg='indigo')
    frame_1.pack(side='top', fill='both')
    # frame2
    frame_2 = Frame(root, width=500, height=450, bg='light grey')
    frame_2.pack(side='top', fill='y')

    # frame_1 Widgets
    name_1 = Label(
        frame_1,
        text='PDF to Audio',
        fg='black', bg='blue',
        font='Arial 28 bold')
    name_1.pack()
    name_2 = Label(
        frame_1,
        text='Hear your PDF File',
        fg='red', bg='indigo',
        font='Arial 28 bold')
    name_2.pack()

    # frame_2 Widgets
    button_1 = Button(
        frame_2,
        text='Select PDF File',
        activeforeground='red',
        command=extract_text,
        padx='70',
        pady='10',
        fg='white',
        bg='black',
        font='Arial 12')
    button_1.grid(row=0, pady=20, columnspan=2)

    rate_text = Label(
        frame_2,
        text="Enter Rate of Speech",
        fg='black',
        bg='aqua',
        font='Arial 12')
    rate_text.grid(row=1, column=0, pady=15, padx=0, sticky=W)

    rate = Entry(
        frame_2,
        text='200',
        fg='black',
        bg='white',
        font='Arial 12')
    rate.grid(row=1, column=1, padx=30, pady=15, sticky=W)

    voice_text = Label(
        frame_2,
        text='Select Voice:',
        fg='black',
        bg='aqua',
        font='Arial 12')
    voice_text.grid(row=2, column=0, pady=15, padx=0, sticky=E)

    male = IntVar()
    male_opt = Checkbutton(
        frame_2,
        text='Male',
        bg='pink',
        variable=male,
        onvalue=1, offvalue=0)
    male_opt.grid(row=2, column=1, pady=0, padx=30, sticky=W)

    female = IntVar()
    female_opt = Checkbutton(
        frame_2,
        text='Female',
        bg='pink',
        variable=female,
        onvalue=1, offvalue=0)
    female_opt.grid(row=3, column=1, pady=0, padx=30, sticky=W)

    submit_button = Button(
        frame_2,
        text='Play PDF File',
        command=speak_text,
        activeforeground='red',
        padx=60,
        pady=10,
        fg='white',
        bg='black',
        font='Arial 12')
    submit_button.grid(row=4, column=0, pady=65)

    stop_button = Button(
        frame_2,
        text='Stop Playing',
        command=stop_speaking,
        activeforeground='red',
        padx=60,
        pady=10,
        fg='white',
        bg='black',
        font='Arial 12')
    stop_button.grid(row=4, column=1, pady=65)


if __name__ == '__main__':

    mytext, rate, male, female = '', 100, 0, 0

    engine = pyttsx3.init()
    root = Tk()
    Application(root)
    root.mainloop()
