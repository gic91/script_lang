import urllib.request
import xml.etree.ElementTree as ET

capitals = {'bg': 'london', 'de': 'berlin', 'fr': 'paris', 'ua': 'kiev', 'es': 'madrid'
            , 'tr': 'ankara', 'iq': 'baghdad', 'ir': 'tehran', 'af': 'kabul', 'sa': 'riyadh'
            , 'ma': 'rabat', 'eg': 'cairo', 'ng': 'abuja', 'ke': 'nairobi', 'za': 'pretoria'
            , 'ru': 'moscow', 'cn': 'beijing', 'in': 'new delhi', 'kr': 'seoul', 'jp': 'tokyo'
            , 'au': 'canberra', 'nz': 'wellington'
            , 'ca': 'ottawa', 'us': 'washington dc.'
            , 'mx': 'mexico city', 'cu': 'havana', 'co': 'bogota', 'br': 'brasilia', 'ar': 'buenos aires'}


capital = urllib.parse.quote(capitals['fr'])
url = "http://api.openweathermap.org/data/2.5/forecast?mode=xml&appid=ee0eb26bb4ce4382c4ba07b8c6f87635&lang=kr&q=" + capital
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if rescode == 200:
    response_body = response.read()
    filename = "capitalweather.xml"
    f = open(filename, "wb")
    f.write(response_body)
    f.close()

    tree = ET.parse(filename)
    weatherdata = tree.getroot()
    sun = weatherdata.find("sun")
    print(sun.attrib)
    for forecast in weatherdata.findall("forecast"):
        for time in forecast:
            print(time.attrib)
            windDirection = time.find("windDirection")
            print(windDirection.attrib)
            windSpeed = time.find("windSpeed")
            print(windSpeed.attrib)
            temperature = time.find("temperature")
            print(temperature.attrib)
            pressure = time.find("pressure")
            print(pressure.attrib)
            humidity = time.find("humidity")
            print(humidity.attrib)
            clouds = time.find("clouds")
            print(clouds.attrib)
else:
    print("Error Code:" + rescode)
