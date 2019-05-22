from bs4 import BeautifulSoup
import urllib.request as req

url = "https://terms.naver.com/entry.nhn?docId=1127117&amp;amp;&cid=40942&categoryId=34082"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

a_list = soup.select("#size_ct > div.att_type > div > div.wr_tmp_profile > div > table > tbody > tr:nth-child(1) > th")
b_list = soup.select("#size_ct > div.att_type > div > div.wr_tmp_profile > div > table > tbody")
print(len(b_list))
for a in b_list:
    name = a.string
    print(name)
