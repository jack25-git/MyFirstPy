from urllib.request import urlopen
url="http://www.baidu.com"
resp=urlopen(url)
content_all=resp.read().decode("utf-8")
with open("../mybaidu.html", mode="w", encoding="utf-8") as f:
    f.write(content_all)


