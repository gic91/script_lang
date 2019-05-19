import game_framework
from tkinter import *
from tkinter import font
import start_state
import Middle_map_state
name = "MenuState"

def enter():
    pass

def update():
    pass
def pause():
    pass
def resume():
    pass
def exit():
    window.destroy()

def center(self):
    w = self.winfo_screenwidth()
    h = self.winfo_screenheight()
    size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2-300
    y = h / 2 - size[1] / 2-400
    self.geometry("%dx%d+%d+%d" % (size + (x, y)))

def process_Euro():
    global main_num
    #대륙별 다른 사진 출력
    Middle_map_state.Main_num(1)
    game_framework.change_state(Middle_map_state)
def process_Asia():
    Middle_map_state.Main_num(2)
    game_framework.change_state(Middle_map_state)
def process_Ocea():
    Middle_map_state.Main_num(3)
    game_framework.change_state(Middle_map_state)
def process_Afri():
    Middle_map_state.Main_num(4)
    game_framework.change_state(Middle_map_state)
def process_N_Amer():
    Middle_map_state.Main_num(5)
    game_framework.change_state(Middle_map_state)
def process_S_Amer():
    Middle_map_state.Main_num(6)
    game_framework.change_state(Middle_map_state)
def process_M_Asia():
    Middle_map_state.Main_num(7)
    game_framework.change_state(Middle_map_state)
def run():
    global window
    window = Tk()
    window.title('세계 지도')
    center(window)
    window.geometry('800x500')  # width x height + 가로격자+세로격자

    main_photo = 'photo\\Main_map.png'
    img = PhotoImage(file=main_photo)

    map_label = Label(window, image=img)
    map_label.pack()
    button1 = Button(window,text = "유럽",command = process_Euro,width= 5)
    button1.place(x=130,y=160)
    button2 = Button(window, text="아시아", command=process_Asia, width=5)
    button2.place(x=245, y=175)
    button3 = Button(window,text = "오세아니아",command = process_Ocea,width= 10)
    button3.place(x=290,y=375)
    button4 = Button(window,text = "아프리카",command = process_Afri,width= 7)
    button4.place(x=75,y=280)
    button5 = Button(window,text = "북아메리카",command = process_N_Amer,width= 10)
    button5.place(x=525,y=170)
    button6 = Button(window,text = "남아메리카",command = process_S_Amer,width= 10)
    button6.place(x=605,y=345)
    button7 = Button(window, text="중동", command=process_M_Asia, width=5)
    button7.place(x=150, y=230)

    chosenFont = font.Font(family='the행복열매', size=20, weight='normal')
    button00 = Button(window, text="X", command=sys.exit, font =chosenFont)
    button00.place(x=760, y=0)
    window.mainloop()




