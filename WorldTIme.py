import urllib.request
import xml.etree.ElementTree as ET


capitals = {'bg': 'europe/london', 'de': 'berlin', 'fr': 'paris', 'ua': 'kiev', 'es': 'madrid'
            , 'tr': 'ankara', 'iq': 'baghdad', 'ir': 'tehran', 'af': 'kabul', 'sa': 'riyadh'
            , 'ma': 'rabat', 'eg': 'cairo', 'ng': 'abuja', 'ke': 'nairobi', 'za': 'pretoria'
            , 'ru': 'moscow', 'cn': 'beijing', 'in': 'new delhi', 'kr': 'seoul', 'jp': 'tokyo'
            , 'au': 'canberra', 'nz': 'wellington'
            , 'ca': 'ottawa', 'us': 'washington dc.'
            , 'mx': 'mexico city', 'cu': 'havana', 'co': 'bogota', 'br': 'brasilia', 'ar': 'buenos aires'}


def info(nation):
    if nation == '영국':
        nation = 'bg'
    elif nation ==  "프랑스":
        nation = 'fr'
    elif nation == "스페인":
        nation = 'es'
    elif nation == "독일":
        nation = 'de'
    elif nation == "우크라이나":
        nation = 'ua'
    elif nation == "러시아":
        nation = 'ru'
    elif nation == "중국":
        nation = 'cn'
    elif nation == "인도":
        nation = 'in'
    elif nation == "일본":
        nation = 'jp'
    elif nation == "대한민국":
        nation = 'kr'
    elif nation == "오스트레일리아":
        nation = 'au'
    elif nation == "뉴질랜드":
        nation = 'nz'
    elif nation == "이집트":
        nation = 'eg'
    elif nation == "남아프리카 공화국":
        nation = 'za'
    elif nation == "모로코":
        nation = 'ma'
    elif nation == "케냐":
        nation = 'ke'
    elif nation == "나이지리아":
        nation = 'ng'
    elif nation == "케나다":
        nation = 'ca'
    elif nation == "미국":
        nation = 'us'
    elif nation == "멕시코":
        nation = 'mx'
    elif nation == "브라질":
        nation = 'br'
    elif nation == "아르헨티나":
        nation = 'ar'
    elif nation == "콜롬비아":
        nation = 'co'
    elif nation == "쿠바":
        nation = 'cu'
    elif nation == "이라크":
        nation = 'iq'
    elif nation == "사우디 아라비아":
        nation = 'sa'
    elif nation == "터키":
        nation = 'tr'
    elif nation == "이란":
        nation = 'ir'
    elif nation == "아프가니스탄":
        nation = 'af'
    capital = urllib.parse.quote(capitals[nation])
    url = "http://worldtimeapi.org/api/timezone/" + capital
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        filename = "worldtime.xml"
        f = open(filename, "wb")
        f.write(response_body)
        f.close()

        tree = ET.parse(filename)
        weatherdata = tree.getroot()

        sun = weatherdata.find("sun")
       # print(sun.attrib)
        w_Sun = sun.attrib
        for forecast in weatherdata.findall("forecast"):
            for time in forecast:
                w_Time.append(time.attrib)
               # print(time.attrib)
                windDirection = time.find("windDirection")
                w_WindD.append(windDirection.attrib)
               # print(windDirection.attrib)
                windSpeed = time.find("windSpeed")
                w_WindS.append(windSpeed.attrib)
               # print(windSpeed.attrib)
                temperature = time.find("temperature")
                w_Tem.append(temperature.attrib)
               # print(temperature.attrib)
                pressure = time.find("pressure")
                w_Pres.append(pressure.attrib)
               # print(pressure.attrib)
                humidity = time.find("humidity")
                w_Pres.append(humidity.attrib)
               # print(humidity.attrib)
                clouds = time.find("clouds")
                w_Cloud.append(clouds.attrib)
               # print(clouds.attrib)


    else:
        print("Error Code:" + rescode)
    return w_Sun,w_Time, w_WindD, w_WindS, w_Tem, w_Pres, w_Cloud
