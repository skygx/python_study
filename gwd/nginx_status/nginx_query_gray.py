# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   nginx_query_gray.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/17 上午10:29   hello      1.0         None

'''
import requests

url = "http://192.168.226.20:8089/query"
params = {
    'status': '2'      #status=1 返回n2 hello!     status=2 返回n3 hello!   没有参数或参数status=0 返回n1 hello!
}

response = requests.get(url, params=params)

print(response.text)
