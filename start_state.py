import game_framework
from tkinter import *
from tkinter import font
import Big_map_state
name = "StartState"

def enter():
    pass

def update():
    pass

def exit():
    window.destroy()
    pass

def process_next():
    game_framework.change_state(Big_map_state)

def run():
    global window
    window = Tk()
    window.title('세계 나라 정보 알리미')
    window.geometry('500x800')  # width x height + 가로격자+세로격자

    main_photo = 'photo\\Main_photo.png'
    img = PhotoImage(file=main_photo)

    map_label = Label(window, image=img)
    map_label.pack()
    chosenFont = font.Font(family='the행복열매', size=40, weight='normal')
    button1 = Button(window,text="시작",command = process_next, font = chosenFont)
    button1.place(x=190,y=650)

    window.mainloop()




