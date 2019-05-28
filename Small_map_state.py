import game_framework
import urllib.request
from tkinter import *
from tkinter import font
from tkinter import Tk, ttk, StringVar, messagebox
import naverapi
import capitalweather
import urllib.request
from PIL import ImageTk, Image
import webbrowser
import openurl

name = "Main"

nation = ""

chapter = 1

def enter():
    ## 백과사전
    global nation
    global description, link, thumbnail
    description, link, thumbnail = naverapi.get_nation_info(nation)
    global nationinfo
    nationinfo = openurl.infotolist(link)

    #날씨
    global w_Sun,w_Time, w_WindD, w_WindS, w_Tem, w_Pres, w_Cloud
    w_Sun,w_Time, w_WindD, w_WindS, w_Tem, w_Pres, w_Cloud = capitalweather.info(nation)
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
#글상자
def TextBox(name,place_x,place_y,size_w,size_y,color,fill):
    t_start = Text(name, width=size_w, height=size_y)
    t_start.config(font="굴림체", foreground=color)
    t_start.insert(1.0, "" +fill )
    t_start.pack(side=LEFT, fill=Y)
    s_start = Scrollbar(name)
    s_start.pack(side=RIGHT, fill=Y)
    s_start.config(command=t_start.yview)
    t_start.config(yscrollcommand=s_start.set)
    name.pack(side=LEFT, fill=Y)
    name.place(x=place_x, y=place_y)
#스크롤 없는 글상자
def TextBox_nonscroll(name,place_x,place_y,size_w,size_y,fill):
    t_start = Text(name, width=size_w, height=size_y)
    t_start.config(font="굴림체")
    t_start.config(font=3)
    t_start.insert(1.0, "" +fill )
    t_start.pack(side=LEFT, fill=Y)
    name.pack(side=LEFT, fill=Y)
    name.place(x=place_x, y=place_y)

#화면 지우개
def erase(y):
    ###다른 함수로갔을때 잔상이 남아있는문제
    ###지우는 법을 못찾겠어서 빈글자로 덮어버림
    ###국기도 다시 불러온다
    chosenFont = font.Font(family='굴림체', size=1000, weight='normal')
    firstNameLabel = Label(window, text="    ", font=chosenFont)  # 국가명
    firstNameLabel.place(x=0, y=y)
    Thunmbnail()

def MakeValue():
    global W_Sun, W_Time, W_WindD, W_WindS, W_Tem, W_Pres, W_Cloud
    W_Time = []
    W_Sun =[]
    W_WindD= []
    W_WindS = []
    W_Tem= []
    W_Cloud= []
    W_Pres= []
    for a, b in zip(range(40),range(40)):
        W_Time.append(list(w_Time[a].values()))
        del(W_Time[a][1])
        W_WindD.append(list(w_WindD[a].values()))
        W_WindS.append(list(w_WindS[a].values()))
        W_Tem.append(list(w_Tem[a].values()))
        W_Pres.append(list(w_Pres[a].values()))
        W_Cloud.append(list(w_Cloud[a].values()))
        W_Sun = list(w_Sun.values())
#국가 백과사전
def ButtonState1():
    window.geometry('500x800')
    erase(30)
    imageLabel.place(x=300, y=35)
    chosenFont = font.Font(family='굴림체', size=20, weight='normal')
    NameLabel = Label(window, text= nation, font=chosenFont,background="black",foreground="white")  # 국가명
    NameLabel.place(x=10, y=30)

    #요약
    box1 = Frame(window)
    TextBox(box1,10,60,33,4,"black",description)
    #표
    for box_key,box_value,b in zip(range(8),range(8),range(8)):
        box_key= Frame(window)
        box_value = Frame(window)
        TextBox_nonscroll(box_key, 10, 180+(b*80), 13, 1,   nationinfo[b][0])
        TextBox(box_value, 100, 180 + (b *80), 15, 3,"blue", nationinfo[b][1])

    for box_key2,box_value2,b2,c in zip(range(8,16),range(8,16),range(8),range(8,16)):
        box_key2= Frame(window)
        box_value2 = Frame(window)
        TextBox_nonscroll(box_key2, 260, 180+(b2*80), 13, 1,   nationinfo[c][0])
        TextBox(box_value2, 355, 180 + (b2 *80), 15, 3,"blue", nationinfo[c][1])

    linkbutton = Button(window, text="네이버 백과사전으로", command=lambda: openwebbrowser(link))
    linkbutton.config(foreground = "blue" )
    linkbutton.place(x=170, y=130)

def clickMe():
     global c_current
     erase(200)
     c_current=combo.current()
     LabelFont = font.Font(family='굴림체', size=20, weight='normal')
     NameLabel2_1 = Label(window, text="바람 방향 :",font= LabelFont )
     NameLabel2_1.place(x=10, y=130)
     NameLabel2 = Label(window, text=W_WindD[c_current],foreground = "blue")
     NameLabel2.place(x=210, y=130)
     NameLabel3_1 = Label(window, text="바람 세기 :",font= LabelFont )
     NameLabel3_1.place(x=10, y=180)
     NameLabel3 = Label(window, text=W_WindS[c_current],foreground = "blue")
     NameLabel3.place(x=210, y=180)
     NameLabel4 = Label(window, text="기온(°C) :",font= LabelFont)
     NameLabel4.place(x=10, y=240)
     NameLabel4 = Label(window, text="%0.2f" % (float(W_Tem[c_current][1])-273.15),foreground = "blue")
     NameLabel4.place(x=210, y=240)
     NameLabel5 = Label(window, text="대기 압 (hPa):",font = LabelFont)
     NameLabel5.place(x=10, y=290)
     NameLabel5 = Label(window, text=W_Pres[c_current],foreground = "blue")
     NameLabel5.place(x=210, y=290)
     NameLabel6 = Label(window, text="구름 :",font = LabelFont)
     NameLabel6.place(x=10, y=340)
     NameLabel6 = Label(window, text=W_Cloud[c_current],foreground = "blue")
     NameLabel6.place(x=210, y=340)
     NameLabel7 = Label(window, text="일출,일몰 :",font = LabelFont)
     NameLabel7.place(x=10, y=390)
     NameLabel7 = Label(window, text=W_Sun,foreground = "blue")
     NameLabel7.place(x=210, y=390)
     print(c_current)
#날씨 &시간
def ButtonState2():
    window.geometry('500x800')
    erase(30)
    MakeValue()
    chosenFont = font.Font(family='굴림체', size=20, weight='normal')
    NameLabel = Label(window, text=nation, font=chosenFont, background="black", foreground="white")  # 국가명
    NameLabel.place(x=10, y=30)

    global combo
    str = StringVar()
    combo = ttk.Combobox(window, width=20, textvariable=str, values=W_Time)
    combo.place(x=10, y=100)
    buttonTime = Button(window, text="확인", command=clickMe)
    buttonTime.place(x=180, y=95)



#항공편
def ButtonState3():
    pass
#사진 불러오기 함수
def Thunmbnail():
    global imageLabel
    imageLabel = Label(window, image=img)
    #####
def run():
    #### 창 만들기
    global window
    window = Toplevel()
    map_label = Label(window)
    map_label.pack()
    center(window)
    window.geometry('500x500')  # width x height + 가로격자+세로격자

    global img
    description, link, thumbnail = naverapi.get_nation_info(nation)
    image = "thumbnail.jpg"
    mem = urllib.request.urlopen(thumbnail).read()
    with open(image, mode="wb") as f:
        f.write(mem)
    img = ImageTk.PhotoImage(Image.open(image))


    Thunmbnail()

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




