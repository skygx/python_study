#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   selenum_test.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/27  9:36   xguo      1.0         None

'''

from selenium import webdriver

import time

def main():


    # 创建Chrome浏览器对象，这会在电脑中打开一个窗口
    browser = webdriver.Chrome(r'C:\Users\xin\AppData\Local\Programs\Python\Python37\chromedriver.exe')

    # 通过浏览器向服务器发起请求
    browser.get('https://www.baidu.com')

    time.sleep(3)

    # 刷新浏览器
    browser.refresh()

    # 最大化浏览器窗口
    browser.maximize_window()

    # 设置链接内容
    element = browser.find_element_by_link_text('抗击肺炎')

    # 点击'抗击肺炎'
    element.click()


if __name__ == "__main__":
    main()