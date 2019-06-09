from datetime import datetime
import threading

gmt = {"영국": -8, "프랑스": -7, "스페인": -7, "독일": -7,"노르웨이":-7,"체코":-7,"이탈리아":-7,"핀란드":-6,"우크라이나": -6,
       "러시아": -6, "중국": -1, "인도": -3, "일본": 0, "대한민국": 0,"몽골": -1,"필리핀": -1,
       "오스트레일리아": +1, "뉴질랜드": +3,
       "이집트": -7, "남아프리카 공화국": -7, "모로코": -9, "케냐": -6, "나이지리아": -8,
       "케나다": -13, "미국": -13,
       "멕시코": -14, "브라질": -12, "아르헨티나": -12, "콜롬비아": -14, "쿠바": -13,
       "이라크": -6, "사우디 아라비아": -6, "터키": -6, "이란": -4, "아프가니스탄": -4}

nation = ""
t = None
def nowtime():
    global nation
    global t
    #t = threading.Timer(1, nowtime)
    #t.start()
    now = datetime.now()
    second = now.second
    changehour = 0
    changeday = 0
    if nation == "인도" or nation == "이란" or nation == "아프가니스탄":
        minute = now.minute - 30
    else:
        minute = now.minute
    if minute < 0:
        minute = 60 + minute
        changehour = -1
    hour = now.hour + changehour + gmt[nation]
    if hour < 0:
        hour = 24 + hour
        changeday = -1
    day = now.day + changeday
    month = now.month
    year = now.year

    time = "%s:%s:%s" % (hour, minute, second)
    return time
