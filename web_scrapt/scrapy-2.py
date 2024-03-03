#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   scrapy-2.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/12  16:49   xguo      1.0         None

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bsObj=BeautifulSoup(html,features="lxml")
    nameList=bsObj.findAll("span",{"class": "green"})
    # nameList=bsObj.findAll(class_="green")
    # nameList=bsObj.find("table",{"id":"giftList"}).tr.next_siblings
    # print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
    for name in nameList:
        print(name.get_text())

if __name__ == "__main__":
    main()