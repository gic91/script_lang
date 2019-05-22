from bs4 import BeautifulSoup
import bs4
import urllib.request as req


def infotolist(link):
    info = []
    key = ""
    value = ""

    url = link
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")

    infochart = soup.select("#size_ct > div.att_type > div > div.wr_tmp_profile > div > table > tbody")

    # size_ct > div.att_type > div > div.wr_tmp_profile > div > table > tbody
    for tr_nth_child in infochart:
        # size_ct > div.att_type > div > div.wr_tmp_profile > div > table > tbody > tr:nth-child(1)
        for thandtd in tr_nth_child:
            for elements in thandtd:
                for element in elements:
                    # size_ct > div.att_type > div > div.wr_tmp_profile > div > table > tbody > tr:nth-child(1) > th > span
                    if type(element) == bs4.element.Tag:
                        for text in element:
                            key = text
                    # size_ct > div.att_type > div > div.wr_tmp_profile > div > table > tbody > tr:nth-child(1) > td
                    elif type(element) == bs4.element.NavigableString:
                        value = element.strip()
                    if key != "" and value != "":
                        info.append([key, value])
                        key = ""
                        value = ""

    return info
