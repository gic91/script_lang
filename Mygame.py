import game_framework
import urllib.request
from tkinter import *
from tkinter import font
from tkinter import Tk, ttk, StringVar,messagebox

name = "Main"

def enter():
    global city
    pass

def exit():
    pass


def run():
    global window
    window = Tk()
    window.title('메인화면')
    window.geometry('500x800')  # width x height + 가로격자+세로격자

    map = 'map.png'
    img = PhotoImage(file=map)

    map_label = Label(window, image=img)
    map_label.pack()


    button1 = Button(window, text="출발지 선택", width=50)
    button1.place(x=100, y=100)

    button2 = Button(window, text="도착지 선택")
    button2.place(x=200, y=200)


    window.mainloop()


def pause():
    pass


def resume():
    pass







