# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   nginx_status.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/7/25 上午9:13   hello      1.0         None

'''
import urllib.request
import re
import time

url = 'http://192.168.226.20:80/nginx_status'

while True:
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    # print(html)
    connections = re.findall(r'connections:\s+(\d+)', html)
    # print(connections)# requests信息
    requests = re.findall(r'\s+(\d+)\s+(\d+)\s+(\d+)', html)  # bytes信息
    # print(requests)
    print('connections:{} | requests:{}'.format(connections, requests[0][2]))
    time.sleep(5)    # 每5秒更新一次
