#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   yanzhao.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/13  20:22   xguo      1.0         None

'''

'''
//  根目录 div  a  li 
[]  谓语   -    条件    class="content-box clearfix"
/   选择元素     
@   提取元素
<ul class="news-list">
                                 <li><span class="span-time">2021-03-12</span>
                                  <a target="_blank" href="/kyzx/fstj/202103/20210312/2037412342.html">2021年考研复试将至，来看看你需要做哪些准备</a>

//ul[@class="new-list”]/li/a/@href   获取href链接地址
'''

import requests
from lxml import etree

def main():
    url = "https://yz.chsi.com.cn/kyzx/fstj/"
    req = requests.get(url).content.decode('utf-8')

    # doc = etree.HTML(req)
    # href_url = doc.xpath('//ul[@class="news-list“]/li/a/@href ')
    doc = etree.parse(req,etree.HTMLParser())
    href_url  = doc.xpath('//ul[@class="news-list"]/li/a/@href ')
    # print(href_url)

    for tony in href_url:
        print(tony)
    # print(req)


if __name__ == "__main__":
    main()