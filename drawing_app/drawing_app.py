import tkinter as tk
import tkinter.ttk as ttk


class FreeHandDrawing(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Free Hand Drawing Tool')
        self.geometry('600x600')
        self._xold = None
        self._yold = None
        self.canvas = None
        self.color = None
        self.thickness = 1
        self.tag = ['tag', '0']
        self._create_widgets()

    def _create_widgets(self):
        top_frame = tk.Frame(self)
        top_frame.grid(row=0, column=0, pady=10)

        self.color_select = tk.StringVar()
        color_list = ttk.Combobox(
            top_frame,
            textvariable=self.color_select,
            values=['Black', 'Green', 'Brown', 'Red', 'Yellow'],
            state="readonly",
            width=10)
        color_list.current(0)
        self.option_add('*TCombobox*Listbox.selectBackground', 'skyblue')
        color_list.bind('<<ComboboxSelected>>', self._change_color)
        color_list.grid(row=0, column=0, padx=5)

        self.t_select = tk.StringVar()
        t_list = ttk.Combobox(
            top_frame,
            textvariable=self.t_select,
            values=[1, 2, 3, 4, 5, 6, 7],
            state="readonly",
            width=3)
        t_list.current(0)
        t_list.bind('<<ComboboxSelected>>', self._change_thickness)
        t_list.grid(row=0, column=1, padx=5)

        tk.Button(
            top_frame,
            text='Undo',
            bg='blue',
            fg='white',
            activebackground='blue4',
            activeforeground='white',
            command=self._undo).grid(
                row=0, column=2, padx=5)
        tk.Button(
            top_frame,
            text='Clear',
            bg='brown',
            fg='white',
            activebackground='brown4',
            activeforeground='white',
            command=self._clear).grid(
                row=0, column=3, padx=5)

        self.canvas = tk.Canvas(self, width=500, height=500, bg='white')
        self.canvas.grid(row=1, column=0, padx=10, pady=(0, 10))
        self.canvas.bind("<ButtonRelease-1>", self._on_release)
        self.canvas.bind("<B1-Motion>", self._on_movement)
        self.canvas.bind("<B3-Motion>", self._undo)

    def _change_color(self, event=None):
        print('_change_color')
        self.color = self.color_select.get()

    def _change_thickness(self, event=None):
        print('_change_thickness')
        self.thickness = int(self.t_select.get())

    def _undo(self, event=None):
        print('undo')
        current_tag = int(self.tag[1])
        if current_tag >= 1:
            self.canvas.delete('tag' + str(current_tag-1))
            self.tag = ['tag', '0']

    def _clear(self):
        print('clear')
        self.canvas.delete('all')
        self.tag = ['tag', '0']

    def _on_release(self, event):
        print('soltei')
        print(self.color)
        self._xold = None
        self._yold = None
        self.tag = ['tag', str(int(self.tag[1])+1)]

    def _on_movement(self, event):
        print('movendo')
        tag = ''.join(self.tag)
        x1, y1 = (event.x - self.thickness), (event.y - self.thickness)
        x2, y2 = (event.x + self.thickness), (event.y + self.thickness)
        event.widget.create_oval(
            x1, y1, x2, y2, width=0, fill=self.color, tag=tag)
        if self._xold is not None and self._yold is not None:
            self.canvas.create_oval(
                x1, y1, x2, y2, width=0, fill=self.color, tag=tag)
            self.canvas.create_line(
                self._xold,
                self._yold,
                event.x,
                event.y,
                smooth=True,
                width=2*self.thickness,
                fill=self.color,
                tag=tag)
            print('dibujo')
        self._xold = event.x
        self._yold = event.y


FreeHandDrawing().mainloop()
