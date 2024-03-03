#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   jd_demo.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/6 下午 8:08   hello      1.0         None

'''

'''
爬虫实战
1.selenium
2.requests.get
3.urllib scrapy

selenium: 自动化测试 框架，模块
项目步骤：
1.访问京东：
访问浏览器--输入京东网站访问--定位搜索框--输入关键字--点击回车
2.抓取信息：
定位商品信息--抓取
'''

from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import  By

import time

def spider(url,keyword):    #自定义爬虫名称和参数
    driver = webdriver.Chrome() #指定浏览器
    driver.get(url)   #发送请求
    input_tag = driver.find_element(By.ID, 'key')    #定位元素
    input_tag.send_keys(keyword) #模拟键盘输入关键字
    input_tag.send_keys(Keys.ENTER) #输入回车

    time.sleep(5)
    get_goods(driver)   #调用抓取商品信息

def get_goods(driver):
    goods = driver.find_elements(By.CLASS_NAME, "gl-item")   #定位每一个商品
    #详情页地址 商品名字 价格 评论数 图片地址
    for good in goods:
        link = good.find_element(By.TAG_NAME, "a").get_attribute('href')    #定位a标签属性
        name = good.find_element(By.CSS_SELECTOR, ".p-name em").text.replace('\n','')    #定位div下em标签
        price = good.find_element(By.CSS_SELECTOR,".p-price i").text
        comment = good.find_element(By.CSS_SELECTOR, ".p-commit strong").text
        img = good.find_element(By.CSS_SELECTOR, ".p-img a img").get_attribute('src')
        msg = '''
            链接: %s
            名字: %s
            价格: %s
            评论数：%s
            图片地址： %s
        ''' % (link, name, price, comment,img)
        print(msg)

if __name__ == '__main__':
    spider('https://www.jd.com/', keyword='苹果13')

