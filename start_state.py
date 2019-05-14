import game_framework
from tkinter import *
import Mygame
name = "StartState"

def enter():
    pass

def update():
    pass

def exit():
    window.destroy()
    pass

def process_next():
    game_framework.change_state(Mygame)

def run():
    global window
    window = Tk()
    window.title('전국 톨게이트 알리미')
    window.geometry('500x800')  # width x height + 가로격자+세로격자

    main_photo = 'main.png'
    img = PhotoImage(file=main_photo)

    map_label = Label(window, image=img)
    map_label.pack()
    button1 = Button(window,text="시작",command = process_next)
    button1.place(x=250,y=750)

    window.mainloop()




