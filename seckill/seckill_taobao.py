import datetime
import time
import os
import pickle
from csv import excel

from selenium import webdriver #操作浏览器
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

chrome_url="D:/chrome/chromedriver-win64/chromedriver-win64/chromedriver.exe"
targ_url="https://www.taobao.com/"

targ_time="2025-03-31 21:22:00.000000000"

cart_url="https://cart.taobao.com/cart.htm"

service=Service(chrome_url)
driver=webdriver.Chrome(service=service)

# driver.get(targ_url)
# time.sleep(3)
# driver.find_element(By.LINK_TEXT, "亲，请登录").click()
# print("请扫码登录")
# time.sleep(20)#等待扫码登录

driver.get(cart_url)
time.sleep(20)#扫描并等待页面加载
try:
    if driver.find_element(By.CLASS_NAME, "ant-checkbox-input"):
        driver.find_element(By.CLASS_NAME, "ant-checkbox-input").click()
        print("全选成功")
except:
    print(f"未找到全选框")

while True:
    now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now_time)
    if now_time>targ_time:
        try:
            if driver.find_element(By.CLASS_NAME,"btn--QDjHtErD"):
                print("找到结算")
                driver.find_element(By.CLASS_NAME,"btn--QDjHtErD").click()
                print("进入结算页面")
                break
        except:
            print("进入结算失败")
            break
    else:
        time.sleep(1)
while True:
    try:
        if driver.find_element(By.CLASS_NAME,"btn--QDjHtErD  "):
            print("找到提交订单")
            driver.find_element(By.CLASS_NAME,"btn--QDjHtErD  ").click()
            print("提交订单成功")
            break
    except:
        print("提交订单失败")
    time.sleep(0.1)


input("请输入")

