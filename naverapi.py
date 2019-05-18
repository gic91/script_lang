import os
import sys
import urllib.request
#from xml.dom.minidom import *
import xml.etree.ElementTree as ET

#def search(nation):
client_id = "qsaDRCTIO8_Ed7ncZYC7"
client_secret = "PMhyq5k9vj"
encText = urllib.parse.quote("독일")#nation)
display = urllib.parse.quote("1")
url = "https://openapi.naver.com/v1/search/encyc.xml?query=" + encText + "&display=" + display
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    filename = "encyc.xml"
    f = open(filename, "wb")
    f.write(response_body)
    f.close()

    tree = ET.parse(filename)
    root = tree.getroot()

    for element in root.findall("channel"):
        item = element.find("item")
        print(item.findtext("description").replace("<b>"+"독일"+"</b>", "독일"))
        print(item.findtext("link"))

        #print(response_body.decode('utf-8'))
        #doc = parseString(response_body.decode('utf-8'))
        #doc.toxml()
        #print(doc.getElementsByTagName("link"))
else:
     print("Error Code:" + rescode)