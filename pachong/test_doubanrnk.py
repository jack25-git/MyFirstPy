import re
import csv
import requests
url='https://movie.douban.com/top250'
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
res=requests.get(url,headers=headers)
content=res.text
pat=re.compile(r'<li>.*?<span class="title">(?P<title>.*?)</span>.*?'
               r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>',re.S)
result=pat.finditer(content)
f=open("data_douban250.csv", mode="w", encoding="utf-8", newline="")
csvwriter=csv.writer(f)
for i in result:
    dic=i.groupdict()
    csvwriter.writerow(dic.values())
    print(dic.values())

res.close()
f.close()