# import csv
# import requests
# from lxml import etree
# from concurrent.futures import ThreadPoolExecutor
# f=open("data_ygzapm.csv",mode="w",encoding="utf-8",newline='')
# csvwriter=csv.writer(f)
#
#
# def download_one_page(url):
#     res=requests.post(url=url)
#     html=etree.HTML(res.text)
#     tab=html.xpath("/html/body/div[4]/div/div[2]/div[1]/div/table")[0]
#     type=tab.xpath("./tr")
#     for i in type:
#         cont=i.xpath("./td/text()")
#         csvwriter.writerow(cont)
#
#     print(url,"提取完毕！")
# if __name__ == '__main__':
#     with ThreadPoolExecutor(1) as t:
#         for i in range(1,20):
#             t.submit(download_one_page(f"http://www.ygzapm.com/web/dailyPrice?totalPageCount=11593&pageNow={i}&product=&typeCode="))
#
# f.close()

from concurrent.futures import ThreadPoolExecutor

def fn(name):
    for i in range(1,200):
        print(name,i)

if __name__ == '__main__':
    with ThreadPoolExecutor(1) as t:
        for i in range(1,50):
            t.submit(fn(f"线程{i}"))
    print("结束")