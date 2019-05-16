import game_framework
import urllib.request
import Big_map_state
from tkinter import *
from tkinter import font
from tkinter import Tk, ttk, StringVar,messagebox

name = "Main"

#대륙별 다른 번호 부여
def Main_num(num):
    global main_num
   # main_num = num

def enter():
    global city
    pass

def exit():
    pass
def pause():
    pass
def process_Euro():
    game_framework.run(Big_map_state)

def run():
    global window,main_num
    window = Tk()
    main_num = 1
    if main_num==1:
        window.title('유럽')
        main_photo = 'photo\\Europe.png'
    elif main_num==2:
        window.title('아시아')
        main_photo = 'photo\\Asia.png'
    elif main_num==3:
        window.title('오세아니아')
        main_photo = 'photo\\Oseania.png'
    elif main_num==4:
        window.title('아프리카')
        main_photo = 'photo\\Africa.png'
    elif main_num==5:
        window.title('북아메리카')
        main_photo = 'photo\\N_America.png'
    elif main_num==6:
        window.title('남아메리카')
        main_photo = 'photo\\S_America.png'
    elif main_num==7:
        window.title('중동')
        main_photo = 'photo\\M_Asia.png'
    img = PhotoImage(file=main_photo)
    map_label = Label(window, image=img)
    map_label.pack()
    if main_num==1:
        nation1 = Button(window, text="영국", width=5)
        nation1.place(x=250, y=320)
        nation2 = Button(window, text="프랑스", width=5)
        nation2.place(x=250, y=355)
        nation3 = Button(window, text="스페인", width=7)
        nation3.place(x=250, y=430)
        nation4 = Button(window, text="독일", width=5)
        nation4.place(x=300, y=320)
        nation5 = Button(window, text="우크라이나", width=10)
        nation5.place(x=380, y=350)
    elif main_num==2:
        nation1 = Button(window, text="1", width=50)
        nation1.place(x=00, y=0)
        nation2 = Button(window, text="2", width=50)
        nation2.place(x=00, y=0)
        nation3 = Button(window, text="3", width=50)
        nation3.place(x=00, y=0)
        nation4 = Button(window, text="4", width=50)
        nation4.place(x=00, y=0)
        nation5 = Button(window, text="5", width=50)
        nation5.place(x=00, y=0)
    elif main_num==3:
        nation1 = Button(window, text="1", width=50)
        nation1.place(x=00, y=0)
        nation2 = Button(window, text="2", width=50)
        nation2.place(x=00, y=0)
        nation3 = Button(window, text="3", width=50)
        nation3.place(x=00, y=0)
        nation4 = Button(window, text="4", width=50)
        nation4.place(x=00, y=0)
        nation5 = Button(window, text="5", width=50)
        nation5.place(x=00, y=0)
    elif main_num==4:
        nation1 = Button(window, text="1", width=50)
        nation1.place(x=00, y=0)
        nation2 = Button(window, text="2", width=50)
        nation2.place(x=00, y=0)
        nation3 = Button(window, text="3", width=50)
        nation3.place(x=00, y=0)
        nation4 = Button(window, text="4", width=50)
        nation4.place(x=00, y=0)
        nation5 = Button(window, text="5", width=50)
        nation5.place(x=00, y=0)
    elif main_num==5:
        nation1 = Button(window, text="1", width=50)
        nation1.place(x=00, y=0)
        nation2 = Button(window, text="2", width=50)
        nation2.place(x=00, y=0)
        nation3 = Button(window, text="3", width=50)
        nation3.place(x=00, y=0)
        nation4 = Button(window, text="4", width=50)
        nation4.place(x=00, y=0)
        nation5 = Button(window, text="5", width=50)
        nation5.place(x=00, y=0)
    elif main_num==6:
        nation1 = Button(window, text="1", width=50)
        nation1.place(x=00, y=0)
        nation2 = Button(window, text="2", width=50)
        nation2.place(x=00, y=0)
        nation3 = Button(window, text="3", width=50)
        nation3.place(x=00, y=0)
        nation4 = Button(window, text="4", width=50)
        nation4.place(x=00, y=0)
        nation5 = Button(window, text="5", width=50)
        nation5.place(x=00, y=0)
    elif main_num==7:
        nation1 = Button(window, text="1", width=50)
        nation1.place(x=00, y=0)
        nation2 = Button(window, text="2", width=50)
        nation2.place(x=00, y=0)
        nation3 = Button(window, text="3", width=50)
        nation3.place(x=00, y=0)
        nation4 = Button(window, text="4", width=50)
        nation4.place(x=00, y=0)
        nation5 = Button(window, text="5", width=50)
        nation5.place(x=00, y=0)
    window.geometry('800x500')  # width x height + 가로격자+세로격자
    button1 = Button(window, text="뒤로가기 아직안댐", width=50, command = process_Euro)
    button1.place(x=00, y=0)


    window.mainloop()


def pause():
    pass


def resume():
    pass







