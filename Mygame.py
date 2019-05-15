import game_framework
import urllib.request
import map_state
from tkinter import *
from tkinter import font
from tkinter import Tk, ttk, StringVar,messagebox

name = "Main"

#대륙별 다른 번호 부여
def Main_num(num):
    global main_num
    main_num = num

def enter():
    global city
    pass

def exit():
    pass
def pause():
    pass
def process_Euro():
    game_framework.change_state(map_state)

def run():
    global window,main_num
    window = Tk()

    if main_num==1:
        window.title('유럽')
        main_photo = 'photo\\Main_map.png'
    elif main_num==2:
        window.title('아시아')
        main_photo = 'photo\\Main_map.png'
    elif main_num==3:
        window.title('오세아니아')
        main_photo = 'photo\\Main_map.png'
    elif main_num==4:
        window.title('아프리카')
        main_photo = 'photo\\Main_map.png'
    elif main_num==5:
        window.title('북아메리카')
        main_photo = 'photo\\Main_map.png'
    elif main_num==6:
        window.title('남아메리카')
        main_photo = 'photo\\Main_map.png'
    elif main_num==7:
        window.title('중동')
        main_photo = 'photo\\Main_map.png'


    img = PhotoImage(file=main_photo)
    map_label = Label(window, image=img)
    map_label.pack()
    window.geometry('800x500')  # width x height + 가로격자+세로격자
    button1 = Button(window, text="출발지 선택", width=50, command = process_Euro)
    button1.place(x=100, y=100)


    window.mainloop()


def pause():
    pass


def resume():
    pass







