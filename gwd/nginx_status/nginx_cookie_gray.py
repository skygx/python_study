# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   nginx_cookie_gray.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/17 上午10:19   hello      1.0         None

'''
import requests

url = 'http://192.168.226.20:8089'
cookies = {'is_gray': '0'}  # 将'cookie_name'和'cookie_value'替换为实际的cookie名称和值
# cookies = {'is_gray': '1'}  # 将'cookie_name'和'cookie_value'替换为实际的cookie名称和值

response = requests.get(url, cookies=cookies)
print(response.text)  # 打印响应内容
