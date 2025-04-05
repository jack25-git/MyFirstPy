import requests
from lxml import etree

#代理 https://www.zdaye.com/free/
#代理 http://www.kxdaili.com/dailiip/2/1.html
proxies={
    "http":"120.197.40.219:9002"
}
url="https://www.zbj.com/fw/?k=saas"
res=requests.get(url,proxies=proxies)
# print(res.text)
html=etree.HTML(res.text)
#拿到每个服务商的div
divs=html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div')
# //*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div
# //*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[5]/div/div/div
# //*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/span
for div in divs:
    price=div.xpath('./div/div[3]/div[1]/span/text()')
    com=div.xpath('./div/div[5]/div/div/div/text()')
    print(com+price)
    break



res.close()