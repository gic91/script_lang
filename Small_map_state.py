import game_framework
import urllib.request
from tkinter import *
from tkinter import font
from tkinter import Tk, ttk, StringVar, messagebox
import naverapi
import urllib.request
from PIL import ImageTk, Image
import webbrowser
import openurl

name = "Main"

nation = ""

chapter = 1

def enter():
    global nation
    global description, link, thumbnail
    description, link, thumbnail = naverapi.get_nation_info(nation)
    global nationinfo
    nationinfo = openurl.infotolist(link)

    run()


# 창 가운데로 정렬
def center(self):
    w = self.winfo_screenwidth()
    h = self.winfo_screenheight()
    size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2 - 200
    y = h / 2 - size[1] / 2 - 550
    self.geometry("%dx%d+%d+%d" % (size + (x, y)))


def openwebbrowser(link):
    webbrowser.open(link)

def TextBox(name,place_x,place_y,size_w,size_y,color,fill):
    t_start = Text(name, width=size_w, height=size_y)
    t_start.config( foreground=color)
    t_start.insert(1.0, "" +fill )
    t_start.pack(side=LEFT, fill=Y)
    s_start = Scrollbar(name)
    s_start.pack(side=RIGHT, fill=Y)
    s_start.config(command=t_start.yview)
    t_start.config(yscrollcommand=s_start.set)
    name.pack(side=LEFT, fill=Y)
    name.place(x=place_x, y=place_y)
def TextBox_nonscroll(name,place_x,place_y,size_w,size_y,fill):
    t_start = Text(name, width=size_w, height=size_y)
    t_start.insert(1.0, "" +fill )
    t_start.pack(side=LEFT, fill=Y)
    name.pack(side=LEFT, fill=Y)
    name.place(x=place_x, y=place_y)
#국가 백과사전
def ButtonState1():
    window.geometry('500x1000')

    imageLabel.place(x=300, y=35)
    chosenFont = font.Font(family='굴림체', size=20, weight='normal')
    NameLabel = Label(window, text= nation, font=chosenFont)  # 국가명
    NameLabel.place(x=30, y=30)

    #요약
    box1 = Frame(window)
    chosenFont = font.Font(family='굴림체', size=2, weight='normal')
    TextBox(box1,20,60,35,5,"black",description)

    for box_key,box_value,b in zip(range(8),range(8),range(8)):
        box_key= Frame(window)
        box_value = Frame(window)
        TextBox_nonscroll(box_key, 20, 380+(b*80), 10, 1,   nationinfo[b][0])
        TextBox(box_value, 100, 380 + (b *80), 15, 3,"blue", nationinfo[b][1])

    for box_key2,box_value2,b2,c in zip(range(8,16),range(8,16),range(8),range(8,16)):
        box_key2= Frame(window)
        box_value2 = Frame(window)
        TextBox_nonscroll(box_key2, 270, 380+(b2*80), 10, 1,   nationinfo[c][0])
        TextBox(box_value2, 350, 380 + (b2 *80), 15, 3,"blue", nationinfo[c][1])

    linkbutton = Button(window, text="더보기", command=lambda: openwebbrowser(link))
    linkbutton.place(x=250, y=130)

#날씨 &시간
def ButtonState2():
    window.geometry('800x500')
    imageLabel.place(x=100, y=175)
    chosenFont = font.Font(family='굴림체', size=10, weight='normal')
    firstNameLabel = Label(window, text="국가명 " + nation, font=chosenFont)  # 국가명
    firstNameLabel.place(x=10, y=50)

    secondNameLabel = Label(window, text=description, font=chosenFont)  # ....
    secondNameLabel.place(x=20, y=170)

    linkbutton = Button(window, text="더보기", command=lambda: openwebbrowser(link))
    linkbutton.place(x=200, y=50)

#항공편
def ButtonState3():
    chosenFont = font.Font(family='굴림체', size=1000, weight='normal')
    firstNameLabel = Label(window, text="    " , font=chosenFont)  # 국가명
    firstNameLabel.place(x=0, y=35)



    image = "thumbnail.jpg"
    mem = urllib.request.urlopen(thumbnail).read()
    with open(image, mode="wb") as f:
        f.write(mem)
    img = ImageTk.PhotoImage(Image.open(image))
    imageLabel = Label(window, image=img)
    imageLabel.pack()
    #####
def run():
    #### 창 만들기
    global window
    window = Toplevel()
    map_label = Label(window)
    map_label.pack()
    center(window)
    window.geometry('500x500')  # width x height + 가로격자+세로격자

    global description, link, thumbnail, imageLabel
    image = "thumbnail.jpg"
    mem = urllib.request.urlopen(thumbnail).read()
    with open(image, mode="wb") as f:
        f.write(mem)
    img = ImageTk.PhotoImage(Image.open(image))
    imageLabel = Label(window, image=img)
    imageLabel.pack()
    #####
    global nationinfo
    print(nationinfo)




    buttonTime = Button(window, text="국가 백과사전", command=ButtonState1)
    buttonTime.place(x=50, y=0)

    buttonTime2 = Button(window, text="날씨&시간", command=ButtonState2)
    buttonTime2.place(x=220, y=0)

    buttonTime3 = Button(window, text="항공편", command=ButtonState3)
    buttonTime3.place(x=380, y=0)

    chosenFont2 = font.Font(family='굴림체', size=10, weight='normal')
    button00 = Button(window, text="X", command=exit, font=chosenFont2)
    button00.place(x=480, y=0)

    ButtonState1()
    window.mainloop()


def pause():
    pass


def resume():
    pass


def exit():
    window.destroy()


def pause():
    pass




