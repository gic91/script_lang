import game_framework
from tkinter import *
from tkinter import font
import Big_map_state
import sys
name = "StartState"



def enter():
    pass

def update():
    pass

def exit():
    window.destroy()


def process_next():
    game_framework.change_state(Big_map_state)
    pass
def center(self):
    w = self.winfo_screenwidth()
    h = self.winfo_screenheight()
    size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2-300
    y = h / 2 - size[1] / 2-400
    self.geometry("%dx%d+%d+%d" % (size + (x, y)))

def run():
    global window
    window = Tk()
    window.title('세계 나라 정보 알리미')

    center(window)
    window.geometry('500x800')  # width x height + 가로격자+세로격자

    main_photo = 'photo\\Main_photo.png'
    img = PhotoImage(file=main_photo)

    map_label = Label(window, image=img)
    map_label.pack()
    chosenFont = font.Font(family='the행복열매', size=40, weight='normal')
    chosenFont2 = font.Font(family='the행복열매', size=20, weight='normal')
    button1 = Button(window,text="시작",command = process_next, font = chosenFont)
    button1.place(x=190,y=650)

    button2 = Button(window, text="X", command=sys.exit, font=chosenFont2)
    button2.place(x=460, y=0)
    window.mainloop()




