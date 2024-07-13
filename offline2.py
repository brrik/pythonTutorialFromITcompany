import requests
from bs4 import BeautifulSoup

url = "ここにWebサイトのURLを入れる"
req = requests.get(url)

bs = BeautifulSoup(req.text,"html.parser")

news = bs.find_all("div", {"class": "newsBlc"})
for elem in news:
    obj = elem.find("a").get_text()
    print(obj)