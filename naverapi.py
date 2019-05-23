import urllib.request
import xml.etree.ElementTree as ET
import re


def get_nation_info(nation):
    client_id = "qsaDRCTIO8_Ed7ncZYC7"
    client_secret = "PMhyq5k9vj"
    encText = urllib.parse.quote(nation)
    #display = urllib.parse.quote("1")
    url = "https://openapi.naver.com/v1/search/encyc.xml?query=" + encText# + "&display=" + display
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        filename = "encyc.xml"
        f = open(filename, "wb")
        f.write(response_body)
        f.close()

        tree = ET.parse(filename)
        root = tree.getroot()

        channel = root.find("channel")
        items = channel.findall("item")
        for item in items:
            if bool(re.search("cid=40942", item.findtext("link"))):  # cid=40942 두산백과의 링크만 사용
                return item.findtext("description").replace("<b>"+nation+"</b>", nation), item.findtext("link"), item.findtext("thumbnail")
    else:
        print("Error Code:" + rescode)
