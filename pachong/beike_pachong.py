import datetime
from math import ceil
import requests
from lxml import etree
import re

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "cookie":"select_city=440300; lianjia_ssid=f2e97439-cddd-444f-9c93-7d94cc0f402d; lianjia_uuid=1e081a1e-6603-45b5-b235-4a52fb6355b1; Hm_lvt_b160d5571570fd63c347b9d4ab5ca610=1743512133; HMACCOUNT=5802897BE22EFB73; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22195f16bdc9be0-0ced29844147ec-26011d51-3686400-195f16bdc9c1188%22%2C%22%24device_id%22%3A%22195f16bdc9be0-0ced29844147ec-26011d51-3686400-195f16bdc9c1188%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%E7%BD%91%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wyshenzhen%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; crosSdkDT2019DeviceId=x3ryd1--w7n6e1-lyetprrwrnxk7af-bmkk3oa2b; login_ucid=2000000022746432; lianjia_token=2.00122f2f9a6bd15736038206ab271a6354; lianjia_token_secure=2.00122f2f9a6bd15736038206ab271a6354; security_ticket=D2wvRHQT88255/WGIkFdTeoum4aObNqJPqpCLwDWYCI34l5yVayTMrOHllr3yLs2Ly0r4GUOFV/kpEvz4m+mGQgSV93NGzHUSQEtI4/X2Q3AuVl++tUIbfj4FD57H5uIUzpMsL+35lKerXQ4YDBGo1msTYUrYlCpDzxEX6R9+v0=; ftkrc_=18a28059-8ba5-43e1-a358-4d304d24af19; lfrc_=7471f048-8efa-42c2-8f9c-217249ac885d; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNTEwOGFhMmU1NTgxYzA0ZTY0MmZjODdiZjNlOTc2OTY3ODQwMjQxMzEzMDBmYzQ4M2QyM2QxOTJmZTM3MTE4MzM0N2RhZTE3OGI2NGI3ZmEwZTJhZjMwOTNlOTMzYTc3YTcwMjc1MThhMjFhYzI2YWRmODVkZDBjYTVjODA3NDE2YWYyODQ4NGFlY2NmOTAwMWM2YThjMjU2YjA5ZTM1YWY1YTQzZmQyMTFlY2Q1NDdhYTMzODUzNjdmNjg1NmRjZmE5ZWYyMGMxNDcyNTI1YWI0ODI0ZTEwOGNiNjExYTA3NDg5M2ZiYmE5NzU5NzViMTBhNDA4YWYzMGU4M2RmYlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJlYzQ3ZGM1YlwifSIsInIiOiJodHRwczovL3N6LmtlLmNvbS9lcnNob3VmYW5nLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610=1743512583"
}
p=1 #第几页
ie="ie2"#有电梯
dp="dp1"#商品房
bp=400#最低价
ep=700#最高价
l="l3l4l5" #3/4/5房

targ_url=f'https://sz.ke.com/ershoufang/nanshanqu/pg{p}{dp}{ie}{l}bp{bp}ep{ep}//'
res=requests.get(targ_url,headers=headers)

pat=re.compile(r'<ul class="sellListContent" log-mod="list">(?P<selllist>.*?)</ul>',re.S)
pat2=re.compile(r'<a href=.*?>(?P<community>.*?)</a>.*?'
                      r'<span class="houseIcon"></span>(?P<houseinfo>.*?)</div>.*?'
                r'<span class="">(?P<totalprice>.*?)</span>',re.S)
result = pat.finditer(res.text)
find_num=int(re.findall(r"共找到<span>(?P<find_num>.*?)</span>",res.text)[0].strip())
dates=str(datetime.date.today()).replace("-","")
print(f"今天日期：{dates},一共找到{find_num}个结果,有{ceil(find_num/30)}个页面")
with open(f"beike/{dates}.csv",mode='w',encoding='utf-8') as f:
    for p in range(1,ceil(find_num/30)+1):
        targ_url = f'https://sz.ke.com/ershoufang/nanshanqu/pg{p}{dp}{ie}{l}bp{bp}ep{ep}//'
        res = requests.get(targ_url, headers=headers)
        result = pat.finditer(res.text)
        for item in result:
            text=str(item.group())
            result2=pat2.finditer(text)
            # print(item.group())
            for item2 in result2:
                dic=item2.groupdict()
                community=item2.group("community")
                house_info=item2.group("houseinfo").strip().replace(" ","").replace("\n","")
                total_price=item2.group("totalprice").strip()
                house_list=house_info.split("|")
                if(len(house_list)==5):#部分数据缺失，导致异常
                    area=float(house_list[3].replace("平米",""))
                    avg_price=float(total_price)/area
                    house_list.append(community)
                    house_list.append(total_price)
                    house_list.append(str(avg_price))
                    house_list.append(str(area))
                else:
                    house_list.append(community)
                    house_list.append(total_price)
                f.write(",".join(house_list)+"\n")
            print(f"写入完成：{targ_url}")