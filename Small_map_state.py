import game_framework
import urllib.request
from tkinter import *
from tkinter import font
from tkinter import Tk, ttk, StringVar, messagebox
import naverapi

name = "Main"

nation = ""
#나라 이름
#def Nation_name(getnation):
    #global nation
    #nation = getnation


def enter():
    global nation
    global description, link
    #국기 가져와서 사진으로 넣기
    description, link = naverapi.get_nation_info(nation)
    run()


def run():
    global description, link
    print(description)
    print(link)
    global window, main_num
    window = Toplevel()
    map_label = Label(window)
    map_label.pack()

    window.geometry('500x500')  # width x height + 가로격자+세로격자
    button1 = Button(window, text="", width=50)
    button1.place(x=00, y=0)

    window.mainloop()


def pause():
    pass


def resume():
    pass


def exit():
    pass


def pause():
    pass




