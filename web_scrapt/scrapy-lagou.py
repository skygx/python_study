#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   scrapy-lagou.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/13  16:29   xguo      1.0         None

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():

    html=urlopen("https://www.lagou.com")
    # print(html.read())
    bsObj=BeautifulSoup(html,features='lxml')
    urlList=bsObj.findAll("span")
    print(urlList)

    for url in urlList:
        print(url.get_text())


if __name__ == "__main__":
    main()