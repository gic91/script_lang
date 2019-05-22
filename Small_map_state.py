import game_framework
import urllib.request
from tkinter import *
from tkinter import font
from tkinter import Tk, ttk, StringVar, messagebox
import naverapi
import urllib.request
from PIL import ImageTk, Image
import webbrowser

name = "Main"

nation = ""


def enter():
    global nation
    global description, link, thumbnail
    # 국기 가져와서 사진으로 넣기
    description, link, thumbnail = naverapi.get_nation_info(nation)
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


def run():
    global description, link, thumbnail
    image = "thumbnail.jpg"
    mem = urllib.request.urlopen(thumbnail).read()
    with open(image, mode="wb") as f:
        f.write(mem)
    global window
    window = Toplevel()
    map_label = Label(window)
    map_label.pack()

    center(window)
    window.geometry('500x500')  # width x height + 가로격자+세로격자

    img = ImageTk.PhotoImage(Image.open(image))
    imageLabel = Label(window, image=img)
    imageLabel.pack()

    chosenFont = font.Font(family='굴림체', size=10, weight='normal')

    firstNameLabel = Label(window, text="국가명 "+nation, font=chosenFont)  # 폰트설정
    firstNameLabel.place(x=30, y=20)

    secondNameLabel = Label(window, text=description, font=chosenFont)  # 폰트설정
    secondNameLabel.place(x=30, y=120)

    chosenFont2 = font.Font(family='굴림체', size=20, weight='normal')
    button00 = Button(window, text="X", command=exit, font=chosenFont2)
    button00.place(x=460, y=0)

    linkbutton = Button(window, text="더보기", command=lambda: openwebbrowser(link))
    linkbutton.pack()


    window.mainloop()


def pause():
    pass


def resume():
    pass


def exit():
    window.destroy()


def pause():
    pass




