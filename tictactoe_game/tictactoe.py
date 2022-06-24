import tkinter as tk


class TICTACTOE(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('TIC TAC TOE')
        self.btns = []
        self.turn = True
        self.count = 0
        self.resizable(width=False, height=False)
        self.Board()

    def Board(self):
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                row.append(tk.Button(
                    self, width=5, height=1, font='Calibre 35 bold',
                    command=lambda x=i, y=j: self.turn_taken(x, y)))
                row[j].grid(row=i, column=j)
            self.btns.append(row)
        tk.Button(
            self, text='New Game', width=10, height=1, font='Calibre 15 bold',
            bg='black', fg='white', activebackground='blue3',
            activeforeground='white', command=self.new_game).grid(
                row=3, column=1)

    def turn_taken(self, x, y):
        self.count += 1
        if self.turn:
            char = 'X'
            self.btns[x][y].config(text='X', bg='black', state='disable')
        else:
            char = 'O'
            self.btns[x][y].config(text='O', bg='grey', state='disable')
        self.ckeck_results(char)
        self.turn = not self.turn

    def new_game(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.btns = []
        self.turn = True
        self.count = 0
        self.resizable(width=False, height=False)
        self.Board()

    def ckeck_results(self, char):
        if ((
            # HORIZONTAL
            (self.btns[0][0]['text'] == char) and
            (self.btns[0][1]['text'] == char) and
            (self.btns[0][2]['text'] == char)) or (
            (self.btns[1][0]['text'] == char) and
            (self.btns[1][1]['text'] == char) and
            (self.btns[1][2]['text'] == char)) or (
            (self.btns[2][0]['text'] == char) and
            (self.btns[2][1]['text'] == char) and
            (self.btns[2][2]['text'] == char)) or (
                # VERTICAL
                (self.btns[0][0]['text'] == char) and
                (self.btns[1][0]['text'] == char) and
                (self.btns[2][0]['text'] == char)) or (
                (self.btns[0][1]['text'] == char) and
                (self.btns[1][1]['text'] == char) and
                (self.btns[2][1]['text'] == char)) or (
                (self.btns[0][2]['text'] == char) and
                (self.btns[1][2]['text'] == char) and
                (self.btns[2][2]['text'] == char)) or (
                    # DIAGONALS
                    (self.btns[0][0]['text'] == char) and
                    (self.btns[1][1]['text'] == char) and
                    (self.btns[2][2]['text'] == char)) or (
                    (self.btns[0][2]['text'] == char) and
                    (self.btns[1][1]['text'] == char) and
                    (self.btns[2][0]['text'] == char))):
            self.result(char)
        elif self.count == 9:
            self.result('Draw')

    def winner(self):
        pass

    def result(self, char):
        top = tk.Toplevel(self)
        if char == "Draw":
            top.title('OOPS!')
            topText = tk.Label(
                top, text='It is a Draw!',
                font='Calibre 30 bold', fg='blue')
        else:
            top.title('Congratulations!')
            topText = tk.Label(
                top, text=f'"{char}" is a Winner!!!',
                font='Calibre 30 bold', fg='blue')
        top_btn = tk.Button(
            top, text='New Game', bg='black', fg='white',
            activebackground='blue3', activeforeground='white',
            command=self.new_game)
        topText.grid(row=0, column=0, padx=10, pady=10)
        top_btn.grid(row=1, column=0)


TICTACTOE().mainloop()
