#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   scrapy-4.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/13  17:53   xguo      1.0         None

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

allExtLinks=set()
allIntLinks=set()

def getAllExternalLinks(siteUrl):
    html=urlopen(siteUrl)
    bsObj=BeautifulSoup(html)
    # internalLinks=getInternal
def main():
    pass

if __name__ == "__main__":
    main()