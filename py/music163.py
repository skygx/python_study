#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   music163.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/11  20:31   xguo      1.0         None

'''

import requests
from lxml import etree


def main():
    url = "https://m701.music.126.net/20210311205517/24ac9e63580510d42ab41344b070880d/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/5624168244/c8e6/b022/3ce4/ea52ffba9c216bc03cfa528ad70c0f59.m4a"

    html= requests.get(url).text
    # print(html)
    #筛选数据（正则，xpath（语法）)
    dom = etree.HTML(html)
    song_ids = dom.xpath('//a[contains(@href,"song?")]/@href')
    song_names = dom.xpath('//a[contains(@href,"song?")]/text()')
    print(song_ids)
    print(song_names)


    #xpath
    # //a[contains(@href,'song?')]/@href
    # //a[contains(@href,'song?')]/text()

    # m4a = requests.get(url).content
    # with open('yinyue.m4a','wb') as file:
    #     file.write(m4a)


if __name__ == "__main__":
    main()