import game_framework
import urllib.request
import Big_map_state
import Small_map_state
from tkinter import *
from tkinter import font
from tkinter import Tk, ttk, StringVar,messagebox
import naverapi

name = "Main"


# 대륙별 다른 번호 부여
def Main_num(num):
    global main_num
    main_num = num

def enter():
   run()

def exit():
   window.destroy()
   pass
def pause():
    pass
def Back():
    window.destroy()
    game_framework.run(Big_map_state)


def center(self):
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2 - 300
        y = h / 2 - size[1] / 2 - 400
        self.geometry("%dx%d+%d+%d" % (size + (x, y)))


def Nation_info(nation):
    Small_map_state.nation = nation
    game_framework.run(Small_map_state)


def run():
    global window,main_num
    window = Tk()
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
    # 29개국 설정
    if main_num == 1:
        nation1 = Button(window, text="영국", width=5, command=lambda: Nation_info("영국"))
        nation1.place(x=250, y=320)
        nation2 = Button(window, text="프랑스", width=5, command=lambda: Nation_info("프랑스"))
        nation2.place(x=250, y=355)
        nation3 = Button(window, text="스페인", width=7, command=lambda: Nation_info("스페인"))
        nation3.place(x=250, y=430)
        nation4 = Button(window, text="독일", width=5, command=lambda: Nation_info("독일"))
        nation4.place(x=300, y=320)
        nation5 = Button(window, text="우크라이나", width=10, command=lambda: Nation_info("우크라이나"))
        nation5.place(x=380, y=350)
        nation6 = Button(window, text="핀란드", width=5, command=lambda: Nation_info("핀란드"))
        nation6.place(x=360, y=235)
        nation7 = Button(window, text="이탈리아", width=6, command=lambda: Nation_info("이탈리아"))
        nation7.place(x=310, y=390)
        nation8 = Button(window, text="노르웨이", width=6, command=lambda: Nation_info("노르웨이"))
        nation8.place(x=280, y=240)
        nation9 = Button(window, text="체코", width=5, command=lambda: Nation_info("체코"))
        nation9.place(x=330, y=350)
    elif main_num == 2:
        nation1 = Button(window, text="러시아", width=5, command=lambda: Nation_info("러시아"))
        nation1.place(x=430, y=140)
        nation2 = Button(window, text="중국", width=5, command=lambda: Nation_info("중국"))
        nation2.place(x=410, y=290)
        nation3 = Button(window, text="인도", width=5, command=lambda: Nation_info("인도"))
        nation3.place(x=345, y=335)
        nation4 = Button(window, text="일본", width=5, command=lambda: Nation_info("일본"))
        nation4.place(x=545, y=290)
        nation5 = Button(window, text="대한민국", width=6, command=lambda: Nation_info("대한민국"))
        nation5.place(x=460, y=295)
        nation6 = Button(window, text="몽골", width=5, command=lambda: Nation_info("몽골"))
        nation6.place(x=410, y=240)
        nation7 = Button(window, text="필리핀", width=5, command=lambda: Nation_info("필리핀"))
        nation7.place(x=490, y=360)
    elif main_num == 3:
        nation1 = Button(window, text="오스트레일리아", width=12, command=lambda: Nation_info("오스트레일리아"))
        nation1.place(x=300, y=270)
        nation2 = Button(window, text="뉴질랜드", width=7, command=lambda: Nation_info("뉴질랜드"))
        nation2.place(x=510, y=380)
    elif main_num == 4:
        nation1 = Button(window, text="이집트", width=5, command=lambda: Nation_info("이집트"))
        nation1.place(x=415, y=110)
        nation2 = Button(window, text="남아프리카 공화국", width=14, command=lambda: Nation_info("남아프리카 공화국"))
        nation2.place(x=400, y=410)
        nation3 = Button(window, text="모로코", width=5, command=lambda: Nation_info("모로코"))
        nation3.place(x=240, y=80)
        nation4 = Button(window, text="케냐", width=5, command=lambda: Nation_info("케냐"))
        nation4.place(x=460, y=250)
        nation5 = Button(window, text="나이지리아", width=9, command=lambda: Nation_info("나이지리아"))
        nation5.place(x=340, y=210)
    elif main_num == 5:
        nation1 = Button(window, text="케나다", width=6, command=lambda: Nation_info("케나다"))
        nation1.place(x=340, y=240)
        nation2 = Button(window, text="미국", width=5, command=lambda: Nation_info("미국"))
        nation2.place(x=380, y=315)
    elif main_num == 6:
        nation1 = Button(window, text="멕시코", width=6, command=lambda: Nation_info("멕시코"))
        nation1.place(x=230, y=25)
        nation2 = Button(window, text="브라질", width=6, command=lambda: Nation_info("브라질"))
        nation2.place(x=450, y=200)
        nation3 = Button(window, text="아르헨티나", width=9, command=lambda: Nation_info("아르헨티나"))
        nation3.place(x=380, y=340)
        nation4 = Button(window, text="콜롬비아", width=7, command=lambda: Nation_info("콜롬비아"))
        nation4.place(x=335, y=135)
        nation5 = Button(window, text="쿠바", width=5, command=lambda: Nation_info("쿠바"))
        nation5.place(x=340, y=25)
    elif main_num == 7:
        nation1 = Button(window, text="이라크", width=7, command=lambda: Nation_info("이라크"))
        nation1.place(x=320, y=165)
        nation2 = Button(window, text="사우디 아라비아", width=13, command=lambda: Nation_info("사우디 아라비아"))
        nation2.place(x=300, y=270)
        nation3 = Button(window, text="터키", width=5, command=lambda: Nation_info("터키"))
        nation3.place(x=250, y=80)
        nation4 = Button(window, text="이란", width=5, command=lambda: Nation_info("이란"))
        nation4.place(x=430, y=170)
        nation5 = Button(window, text="아프가니스탄", width=10, command=lambda: Nation_info("아프가니스탄"))
        nation5.place(x=520, y=160)
    center(window)
    window.geometry('800x500')  # width x height + 가로격자+세로격자
    button1 = Button(window, text="뒤로가기", width=30, command = Back)
    button1.place(x=00, y=0)

    chosenFont = font.Font(family='the행복열매', size=20, weight='normal')
    button00 = Button(window, text="X", command=sys.exit, font=chosenFont)
    button00.place(x=760, y=0)
    window.mainloop()


def pause():
    pass


def resume():
    pass
