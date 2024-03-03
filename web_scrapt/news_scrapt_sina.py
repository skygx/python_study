#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   news_scrapt_sina.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/17 上午 9:05   hello      1.0         None

'''
import requests
import re
from bs4 import BeautifulSoup

class HandleNews(object):
    def __init__(self):
        self.request = requests.session()
        # self.head = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
        #             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        self.header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                     }
        self.newslist = ''

    def handle_list(self):
        handle_url='http://www.sohu.com/c/8'
        handle_news=self.handle_request(methon='GET',url=handle_url,head=self.header)
        soup = BeautifulSoup(handle_news, "html.parser")


    def handle_request(self,methon,url,head,data=None , info=None):
        if methon == 'GET':
            handle_respone=self.request.get(url=url,headers=head)
        else:
            handle_respone=' '
        return handle_respone.text

if __name__ == '__main__':
    handle=HandleNews()
    handle.handle_list()
    print(handle.newslist)
