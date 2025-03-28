# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   nginx_header_gray.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/17 下午12:18   hello      1.0         None

'''

import requests

url = 'http://192.168.226.20:8089/remote'
headers = {
    'X-Forwarded-For': '9.9.9.9'
}

response = requests.get(url, headers=headers)
print(response.text)
