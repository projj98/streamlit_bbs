import requests
from bs4 import BeautifulSoup

for number in range(0,10):
    url = "https://www.clien.net/service/board/park?&od=T31&category=0&po={}".format(number)
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=header)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    bbs_lists = soup.find_all('div', attrs={"class":"list_item symph_row"})

    for bbs_list in bbs_lists:
        title = bbs_list.find('span', attrs={"class":"subject_fixed"})
        reply = bbs_list.find('span', attrs={"class":"rSymph05"})

        try:
            replytext = reply.get_text()
        except: continue

        if int(replytext) >= 10:
            print(title.get("title"))



