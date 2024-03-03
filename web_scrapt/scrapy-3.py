#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   scrapy-3.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/13  16:42   xguo      1.0         None

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages=set()

def getLinks(pageUrl):
    global pages
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj=BeautifulSoup(html)
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage=link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
                
def main():
    getLinks("")
    


if __name__ == "__main__":
    main()