#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   scrap-1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/10  13:14   xguo      1.0         None

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    bsObj=BeautifulSoup(html.read(),features="lxml")
    print(bsObj.h1)


if __name__ == "__main__":
    main()