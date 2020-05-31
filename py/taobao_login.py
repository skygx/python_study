#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   taobao_login.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/27  10:57   xguo      1.0         None

'''

# encoding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class Spider:  # 定义一个叫Spider的类
    def __init__(self, url):
        self.__base_url = url
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}  # 伪装成浏览器

    def get_url(self):  # 获取URL链接，并打开
        global driver
        driver.get(self.__base_url)

    def login(self):
        global driver
        if driver.find_element_by_link_text("亲，请登录"):  # 定位首页的登录文字
            driver.find_element_by_link_text("亲，请登录").click()  # 模拟点击登录
            driver.implicitly_wait(5)
            # time.sleep(2)  #等待一下，避免网页刷新慢时抓不到下面的定位
            driver.find_element_by_xpath(
                "//*[@id='login']/div[1]/div[1]").click()  # 定位登录表单中的切换账户密码位置，因为淘宝的默认登录为二维码扫描
            account = driver.find_element_by_xpath("//*[@id='fm-login-id']")  # 定位用户名输入框
            account.send_keys("13693367745")  # 输入账户
            password = driver.find_element_by_xpath("//*[@id='fm-login-password']")  # 定位密码输入框
            password.send_keys("Gx!2135501")  # 输入密码
            # 以下时尝试处理验证滑块，但失败
            while True:
                try:
                    # 定位滑块元素
                    source = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
                    # 定义鼠标拖放动作
                    ActionChains(driver).drag_and_drop_by_offset(source, 400, 0).perform()
                    # 等待JS认证运行,如果不等待容易报错
                    time.sleep(2)
                    # 查看是否认证成功，获取text值
                    text = driver.find_element_by_xpath("//*[@id='nocaptcha-password']/span")
                    # 目前只碰到3种情况：成功（请在在下方输入验证码,请点击图）；无响应（请按住滑块拖动)；失败（哎呀，失败了，请刷新）
                    if text.text.startswith(u'请在下方'):
                        print('成功滑动')
                        break
                    if text.text.startswith(u'请点击'):
                        print('成功滑动')
                        break
                    if text.text.startswith(u'请按住'):
                        continue
                except Exception as e:
                    # 这里定位失败后的刷新按钮，重新加载滑块模块
                    driver.find_element_by_xpath("//*[@id='nocaptcha-password']/div/span/a").click()
                    print(e)
            time.sleep(3)  # 等待停顿时间
            # driver.find_element_by_xpath("//*[@id='J_SubmitStatic']").click()  # 定位并点击登录按钮
            driver.find_element_by_link_text("登录").click()  # 定位并点击登录按钮

            time.sleep(30)


def main():
    global driver
    chromedriver_path = r"C:\Users\xin\AppData\Local\Programs\Python\Python37\chromedriver.exe"
    option = webdriver.ChromeOptions()  # 创建Chrome浏览器对象
    # option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 设置开发者模式
    # option.add_argument('--start-maximized')  # 最大化运行浏览器
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=option)
    # driver = webdriver.Chrome(chrome_options=option)
    spider = Spider("https://www.taobao.com")
    spider.get_url()
    spider.login()


if __name__ == "__main__":
    main()