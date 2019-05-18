import game_framework
import urllib.request
from tkinter import *
from tkinter import font
from tkinter import Tk, ttk, StringVar,messagebox

name = "Main"

#나라 이름
def Nation_name(name):
    global nation_name
    nation_name = name

def enter():
   run()

def exit():
   pass
def pause():
    pass
def Back():
    pass
def run():
    global window,main_num
    window = Toplevel()
    map_label = Label(window)
    map_label.pack()

    window.geometry('500x500')  # width x height + 가로격자+세로격자
    button1 = Button(window, text="뒤로가기 아직안댐", width=50, command = Back)
    button1.place(x=00, y=0)

    window.mainloop()


def pause():
    pass


def resume():
    pass







