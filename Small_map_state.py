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
    y = h / 2 - size[1] / 2 - 300
    self.geometry("%dx%d+%d+%d" % (size + (x, y)))


def openwebbrowser(link):
    webbrowser.open(link)

def ButtonState1():
    imageLabel.place(x=300, y=75)
    chosenFont = font.Font(family='굴림체', size=10, weight='normal')

    firstNameLabel = Label(window, text="국가명 " + nation, font=chosenFont)  # 국가명
    firstNameLabel.place(x=30, y=70)

    secondNameLabel = Label(window, text=description, font=chosenFont)  # ....
    secondNameLabel.place(x=30, y=170)


    linkbutton = Button(window, text="더보기", command=lambda: openwebbrowser(link))
    linkbutton.pack()


def ButtonState2():
    imageLabel.place(x=100, y=175)
    chosenFont = font.Font(family='굴림체', size=10, weight='normal')

    firstNameLabel = Label(window, text="국가명 " + nation, font=chosenFont)  # 국가명
    firstNameLabel.place(x=230, y=50)

    secondNameLabel = Label(window, text=description, font=chosenFont)  # ....
    secondNameLabel.place(x=330, y=270)

    linkbutton = Button(window, text="더보기", command=lambda: openwebbrowser(link))
    linkbutton.pack()


def ButtonState3():
    pass
def run():
    global description, link, thumbnail
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
    ##### 처음시작은 1번
    ButtonState1()
    ######

    buttonTime = Button(window, text="날씨&시간", command=ButtonState1)
    buttonTime.place(x=80, y=0)

    buttonTime2 = Button(window, text="날씨&시간", command=ButtonState2)
    buttonTime2.place(x=280, y=0)

    buttonTime3 = Button(window, text="날씨&시간", command=ButtonState3)
    buttonTime3.place(x=380, y=0)

    chosenFont2 = font.Font(family='굴림체', size=10, weight='normal')
    button00 = Button(window, text="X", command=exit, font=chosenFont2)
    button00.place(x=480, y=0)

    window.mainloop()


def pause():
    pass


def resume():
    pass


def exit():
    window.destroy()


def pause():
    pass




