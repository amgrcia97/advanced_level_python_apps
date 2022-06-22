import tkinter as tk


Keyboard_App = tk.Tk()
Keyboard_App.title('Keyboard Application')

keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=',
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'DEL',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"',
        'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '!', 'TAB',
        'SPACE']

current_button = [-1, -1]
button_L = [[]]
entry = tk.Text(Keyboard_App, width=97, height=8)
entry.grid(row=0, columnspan=15)

var_row = 1
var_column = 0


def leftkey(event):
    if current_button == [-1, -1]:
        current_button[:] = [0, 0]
        button_L[0][0].configure(highlightbackground='red')
    elif current_button[0] == 4:
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
        current_button[:] = [0, 10]
        button_L[0][10].configure(highlightbackground='red')
    else:
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
        current_button[:] = [current_button[0], (current_button[1]-1) % 11]
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
    button_L[current_button[0]][current_button[1]].focus_set()


def rightkey(event):
    if current_button == [-1, -1]:
        current_button[:] = [0, 0]
        button_L[0][0].configure(highlightbackground='red')
    elif current_button[0] == 4:
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
        current_button[:] = [0, 0]
        button_L[0][10].configure(highlightbackground='red')
    else:
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
        current_button[:] = [current_button[0], (current_button[1]+1) % 11]
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
    button_L[current_button[0]][current_button[1]].focus_set()


def upkey(event):
    if current_button == [-1, -1]:
        current_button[:] = [0, 0]
        button_L[0][0].configure(highlightbackground='red')
    elif current_button[0] == 0:
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
        current_button[:] = [(current_button[0]-1) % 5, 0]
        button_L[0][10].configure(highlightbackground='red')
    elif current_button[0] == 4:
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
        current_button[:] = [(current_button[0]-1) % 5, 5]
        button_L[0][10].configure(highlightbackground='red')
    else:
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
        current_button[:] = [(current_button[0]-1) % 11, current_button[1]]
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
    button_L[current_button[0]][current_button[1]].focus_set()


def downkey(event):
    if current_button == [-1, -1]:
        current_button[:] = [0, 0]
        button_L[0][0].configure(highlightbackground='red')
    elif current_button[0] == 0:
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
        current_button[:] = [(current_button[0]+1) % 5, current_button[1]]
        button_L[0][10].configure(highlightbackground='red')
    elif current_button[0] == 4:
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
        current_button[:] = [(current_button[0]+1) % 5, 5]
        button_L[0][10].configure(highlightbackground='red')
    elif current_button[0] == 3:
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
        current_button[:] = [(current_button[0]+1) % 5, 0]
        button_L[0][10].configure(highlightbackground='red')
    else:
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
        current_button[:] = [(current_button[0]+1) % 11, current_button[1]]
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
    button_L[current_button[0]][current_button[1]].focus_set()


def select(value, x, y):
    if current_button != [-1, -1]:
        button_L[current_button[0]][current_button[1]].configure(
            highlightbackground='red')
        button_L[current_button[0]][current_button[1]].configure(
            highlightcolor='red')
    current_button[:] = [x, y]
    button_L[x][y].configure(
            highlightbackground='red')
    button_L[x][y].configure(
            highlightcolor='red')

    if value == 'DEL':
        input_val = entry.get('1.0', 'end-2c')
        entry.delete('1.0', 'end')
        entry.insert('1.0', input_val, 'end')
    elif value == 'SPACE':
        entry.insert('insert', ' ')
    elif value == 'TAB':
        entry.insert('insert', '    ')
    else:
        entry.insert('end', value)


for button in keys:
    if button != 'SPACE':
        but = tk.Button(
            Keyboard_App,
            text=button,
            width=5,
            bg='black',
            fg='white',
            highlightthickness=4,
            activebackground='gray',
            activeforeground='red',
            highlightcolor='red',
            relief='raised',
            padx=12,
            pady=4,
            bd=4,
            command=lambda x=button,
            i=var_row-1,
            j=var_column: select(x, i, j))
        but.bind(
            '<Return>',
            lambda event, x=button, i=var_row-1, j=var_column: select(x, i, j))
        button_L[var_row-1].append(but)
        but.grid(row=var_row, column=var_column)

    if button == 'SPACE':
        but = tk.Button(
            Keyboard_App,
            text=button,
            width=60,
            bg='black',
            fg='white',
            highlightthickness=4,
            activebackground='gray65',
            activeforeground='red',
            highlightcolor='red',
            relief='raised',
            padx=4,
            pady=4,
            bd=4,
            command=lambda x=button,
            i=var_row-1,
            j=var_column: select(x, i, j))
        but.bind(
            '<Return>',
            lambda event, x=button, i=var_row-1, j=var_column: select(x, i, j))
        button_L[var_row-1].append(but)
        but.grid(row=6, columnspan=16)

    var_column += 1

    if var_column > 10:
        var_column = 0
        var_row += 1
        button_L.append([])

Keyboard_App.bind('<Left>', leftkey)
Keyboard_App.bind('<Right>', rightkey)
Keyboard_App.bind('<Up>', upkey)
Keyboard_App.bind('<Down>', downkey)


Keyboard_App.mainloop()
