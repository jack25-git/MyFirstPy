import requests
from bs4 import BeautifulSoup

url="http://www.vegnet.com.cn/Channel/Price?flag=12&ename=fanqie"
resp=requests.get(url)
resp.encoding="utf-8"
# print(resp.text)
page=BeautifulSoup(resp.text,"html.parser")
tab=page.find("div",attrs={"class":"right_715"})
# print(tab)
data=tab.find_all("p")[1:]
# print(data)
for i in data:
    veg=i.find_all("span")
    date=veg[0]
    kind=veg[1]
    market=veg[2]
    price=veg[3]
    print(date)
    print(kind)
    print(market)
    print(price)
    break

resp.close()
