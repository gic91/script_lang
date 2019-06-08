import urllib.request
import xml.etree.ElementTree as ET

serviceKey = urllib.parse.quote("ygkIrx1r4KQizK3fX8OLKfu1jTEhwT6eiujXWKMsKcjIVTbriNkC6mHHDZaN0494tUZqOdSnJ9FyCrJjBDCrEA%3D%3D")
# 출발공항 인천, 김포, 제주, 김해, 청주, 대구, 양양, 무안 중 하나
deptCityCode = urllib.parse.quote("GMP")
# 도착공항
# 영국: LHR, 독일: 뮌헨, 프랑스: 파리 샤를 드 골, 우크라이나: 보리스필
# 러시아: 셰레메티예보, 중국: 베이징, 인도: 델리, 일본: 나리타, 오스트레일리아: 시드니
# 뉴질랜드: 오클랜드, 이집트: 카이로, 남아공: 케이프 타운, 모로코: 카사블랑카
# 케냐: 나이로비, 나이지리아: 라고스, 캐나다: 토론토, 미국: ATL, 멕시코: MEX 브라질: GRU
# 아르헨티나: BAS, 콜롬비아: BOG, 쿠바
# 이라크: BGW, 사우디: JED, 터키: IST, 이란: THR, 아프가니스탄: KBL
arrvCityCode = urllib.parse.quote("PUS")
schDate = urllib.parse.quote("20190601")
url = "http://openapi.airport.co.kr/service/rest/FlightScheduleList/getDflightScheduleList?ServiceKey=" + serviceKey \
      + "&schDeptCityCode=" + deptCityCode + "&schArrvCityCode=" + arrvCityCode + "&schDate=" + schDate

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if rescode == 200:
    response_body = response.read()
    filename = "flightScheduleList.xml"
    f = open(filename, "wb")
    f.write(response_body)
    f.close()

    tree = ET.parse(filename)
    root = tree.getroot()
else:
    print("Error Code:" + rescode)