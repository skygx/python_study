#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   grab_taobao.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/27  9:43   xguo      1.0         None

'''

from selenium import webdriver
import time
import re
import csv

browser = webdriver.Chrome()

# 通过浏览器向服务器发起请求
browser.get('https://www.taobao.com/')  # 向服务器发送请求

def search_product(key_word):
    '''


    :param key_word: 搜索关键字
    :return:
    '''

    # 通过id值来获取文本框的位置，并传入关键字
    browser.find_element_by_id('q').send_keys(key_word)
    # 通过class来获取到搜索按钮的位置，并点击
    browser.find_element_by_class_name('btn-search').click()
    # 最大化窗口
    browser.maximize_window()


    time.sleep(15)
    page = browser.find_element_by_xpath('//div[@class="total"]').text  # 共 100 页，


    page = re.findall('(\d+)', page)[0] # findall返回一个列表
    return page


def get_product():
    # divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')# 这里返回的是列表，注意：elements
    divs = browser.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')# 这里返回的是列表，注意：elements
    for div in divs:
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text
        price = div.find_element_by_xpath('.//strong').text + '元'
        nums = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        names = div.find_element_by_xpath('.//div[@class="shop"]/a').text
        print(info, price, nums, names,sep='|')
        with open('data3.csv', mode='a', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file, delimiter=',')    # 指定分隔符为逗号
            csv_writer.writerow([info, price, nums, names])


def main():

    key_word=input('请输入关键字：')
    page = search_product(key_word)
    print('正在爬取第1页的数据')
    get_product()  # 已经获得第1页的数据
    page_nums = 1
    while page_nums != page:
        print('*' * 100)
        print('正在爬取第{}页的数据'.format(page_nums + 1))
        browser.get('https://s.taobao.com/search?q={}&s={}'.format(key_word, page_nums * 44))
        browser.implicitly_wait(10)  # 等待10秒
        get_product()
        page_nums += 1

if __name__ == "__main__":
    main()