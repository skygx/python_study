#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   send_randomip_request.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/19 下午 3:07   hello      1.0         None

'''

import requests
import threading

url = "http://192.168.226.20"

def send_request(ip):
    proxies = {
        'http': f'http://{ip}',
        'https': f'http://{ip}',
    }
    response = requests.get(url, proxies=proxies)
    print(f'Response from {ip}: {response.text}')

ips = ['192.168.0.2', '192.168.0.3', '192.168.0.4']
threads = []
for ip in ips:
    thread = threading.Thread(target=send_request, args=(ip,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
