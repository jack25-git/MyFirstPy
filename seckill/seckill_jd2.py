from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def jd_seckill():
    # 设置 ChromeDriver 路径，需根据实际情况修改
    chrome_driver_path = "D:/chrome/chromedriver-win64/chromedriver-win64/chromedriver.exe"
    service = Service(chrome_driver_path)
    # 创建 Chrome 浏览器实例
    driver = webdriver.Chrome(service=service)

    try:
        # 打开京东登录页面
        driver.get('https://passport.jd.com/new/login.aspx')
        print("请在浏览器中完成登录操作")
        # 等待用户手动完成登录
        input("登录完成后按回车键继续...")

        # 打开购物车页面
        driver.get('https://cart.jd.com/cart.action')
        time.sleep(10)
        # 等待秒杀开始时间
        seckill_time = '2025-03-31 21:50:00'
        # while True:
        #     current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        #     if current_time >= seckill_time:
        #         break
        #     time.sleep(0.1)

        print("开始抢购")
        try:
            # 勾选购物车中要购买的商品，这里假设商品在购物车中第一个位置，可根据实际情况调整选择器
            checkbox = driver.find_element(By.NAME,"select-all")
            checkbox.click()
            print("已勾选商品")
        except Exception as e:
            print(f"勾选商品时出错: {e}")

        # 点击去结算按钮
        try:
            submit_button = driver.find_element(By.CLASS_NAME, 'common-submit-btn')
            submit_button.click()
            print("已点击去结算按钮")
        except Exception as e:
            print(f"点击去结算按钮时出错: {e}")

        # 点击提交订单按钮
        try:
            order_submit = driver.find_element(By.ID, 'order-submit')
            order_submit.click()
            print("已点击提交订单按钮，抢购完成")
        except Exception as e:
            print(f"点击提交订单按钮时出错: {e}")

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 等待一段时间，方便查看结果
        time.sleep(10)
        # 关闭浏览器
        driver.quit()


if __name__ == "__main__":
    jd_seckill()
