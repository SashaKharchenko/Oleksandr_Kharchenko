# 24.47. Скласти програму з графічним інтерфейсом для реалізації простого графічного редактора. Надати можливість зображувати лінії, прямокутники, еліпси заданого кольору та з заданою товщиною та кольором границі.Зберігати параметри зображення у файлі та відновлювати з файлу

from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
import enum
from typing import NamedTuple

class Mode(enum.Enum):
    LINE = 'LINE'
    RECTANGLE = 'RECTANGLE'
    ELLIPSE = 'ELLIPSE'
    
    def __str__(self) -> str:
        return self.value

class HistoryEntry(NamedTuple):
    mode: Mode
    start_x: int
    start_y: int
    end_x: int
    end_y: int
    color_p: str
    color_s: str
    width: int
    
    def __str__(self) -> str:
        return f'{self.mode},{self.start_x},{self.start_y},{self.end_x},{self.end_y},{self.color_p},{self.color_s},{self.width}'
    def __repr__(self) -> str:
        return str(self)
    
    @classmethod
    def from_str(cls, s: str) -> 'HistoryEntry':
        mode, start_x, start_y, end_x, end_y, color_p,color_s, width = s.split(',')
        return cls(
            Mode(mode),
            int(start_x),
            int(start_y),
            int(end_x),
            int(end_y),
            color_p,
            color_s,
            int(width)
        )

def choose_color_p():
    global color_p
    color_p = colorchooser.askcolor()[1]
    update_color_p()

def choose_color_s():
    global color_s
    color_s = colorchooser.askcolor()[1]
    update_color_s()

def update_color_p():
    global color_p
    color_p_btn.config(bg=color_p)

def update_color_s():
    global color_s
    color_s_btn.config(bg=color_s)

def change_mode(new_mode:Mode):
    global mode
    mode = new_mode
    line_btn.config(relief=RAISED)
    rectangle_btn.config(relief=RAISED)
    ellipse_btn.config(relief=RAISED)
    if mode == Mode.LINE:
        line_btn.config(relief=SUNKEN)
    elif mode == Mode.RECTANGLE:
        rectangle_btn.config(relief=SUNKEN)
    elif mode == Mode.ELLIPSE:
        ellipse_btn.config(relief=SUNKEN)

def canvas_hold_start(event:Event):
    global hold_start
    hold_start = (event.x, event.y)

def canvas_hold_end(event:Event):
    global hold_start, history,redo_history
    history.append(HistoryEntry(mode,hold_start[0],hold_start[1],event.x,event.y,color_p,color_s,width_slider.get()))
    redraw()
    redo_history = []

def save():
    global history
    file = filedialog.asksaveasfile(mode='w', defaultextension='.csv', filetypes=[('CSV', '*.csv')])
    if file is None:
        return
    with file:
        for entry in history:
            file.write(str(entry) + '\n')

def load():
    global history
    try:
        file = filedialog.askopenfile(mode='r', filetypes=[('CSV', '*.csv')])
        if file is None:
            return
        with file:
            history = []
            for entry in file.readlines():
                history.append(HistoryEntry.from_str(entry))
            print(history)
        redraw()
    except FileNotFoundError:
        print('File not found')

def redraw():
    canvas.delete('all')
    for entry in history:
        if entry.mode == Mode.LINE:
            canvas.create_line(entry.start_x, entry.start_y, entry.end_x, entry.end_y, fill=entry.color_p, width=entry.width)
        elif entry.mode == Mode.RECTANGLE:
            canvas.create_rectangle(entry.start_x, entry.start_y, entry.end_x, entry.end_y, fill=entry.color_p,outline=entry.color_s, width=entry.width)
        elif entry.mode == Mode.ELLIPSE:
            canvas.create_oval(entry.start_x, entry.start_y, entry.end_x, entry.end_y, fill=entry.color_p,outline=entry.color_s, width=entry.width)

def undo():
    global history, redo_history
    if not history:
        return
    redo_history.append(history.pop())
    redraw()
    
def redo():
    global history, redo_history
    if not redo_history:
        return
    history.append(redo_history.pop())
    redraw()
    

root = Tk()
canvas = Canvas(root, width=500, height=500, bg='white')
# menu with line, rectangle, ellipse and color buttons
menu = Frame(root, bg='white')
save_btn = Button(menu, text='Save', bg='white', command=save)
load_btn = Button(menu, text='Load', bg='white', command=load)
line_btn = Button(menu, text='Line', bg='white', command=lambda: change_mode(Mode.LINE))
rectangle_btn = Button(menu, text='Rectangle', bg='white', command=lambda: change_mode(Mode.RECTANGLE))
ellipse_btn = Button(menu, text='Ellipse', bg='white', command=lambda: change_mode(Mode.ELLIPSE))
color_p_btn = Button(menu, text=' ', bg='black', relief=FLAT,command=choose_color_p, width=2)
color_s_btn = Button(menu, text=' ', bg='black', relief=FLAT,command=choose_color_s, width=2)
width_slider = Scale(menu, from_=1, to=10, orient=HORIZONTAL, bg='white')

undo_btn = Button(menu, text='Undo', bg='white', command=undo)
redo_btn = Button(menu, text='Redo', bg='white', command=redo)

mode = Mode.LINE
color_p = '#000000'
color_s = '#000000'
history: list[HistoryEntry] = []
redo_history: list[HistoryEntry] = []

change_mode(mode) # update buttons
update_color_p() # update color button
update_color_s() # update color button

canvas.bind('<Button-1>', canvas_hold_start)
canvas.bind('<ButtonRelease-1>', canvas_hold_end)

# pack menu
menu.pack(side=TOP, fill=X)
# pack buttons
save_btn.pack(side=LEFT)
load_btn.pack(side=LEFT)
line_btn.pack(side=LEFT)
rectangle_btn.pack(side=LEFT)
ellipse_btn.pack(side=LEFT)
color_p_btn.pack(side=LEFT)
color_s_btn.pack(side=LEFT)
width_slider.pack(side=LEFT)
undo_btn.pack(side=LEFT)
redo_btn.pack(side=LEFT)
# pack canvas
canvas.pack()
root.mainloop()