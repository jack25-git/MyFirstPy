import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_url="D:/chrome/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service=Service(chrome_url)

targ_time="2025-03-31 21:30:00"
cart_url="https://cart.jd.com/cart_index"
driver=webdriver.Chrome(service=service)
driver.get(cart_url)
time.sleep(20)
driver.get(cart_url)
time.sleep(20)
try:
    if driver.find_element(By.NAME,"select-all"):
        driver.find_element(By.NAME,"select-all").click()
        print("全选成功")
except:
    print("全选异常")

while True:
    now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now_time)
    if now_time>targ_time:
        while True:
            try:
                if driver.find_element(By.LINK_TEXT,"去结算"):
                    driver.find_element(By.LINK_TEXT, "去结算").click()
                    print("去结算成功")
                    break
            except:
                print("去结算异常")
                continue
        break
    time.sleep(1)

input("请输入")




