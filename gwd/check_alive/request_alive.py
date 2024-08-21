# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   request_alive.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/21 下午3:13   hello      1.0         None

'''

import requests
def check_port(ip, port):
    try:
        response = requests.get(f"http://{ip}:{port}",timeout=1)
        if response.status_code == 200:
            print(f"端口 {port} 是开放的")
        else:
            print(f"端口 {port} 是关闭的")
    except requests.exceptions.ConnectionError:
        print(f"端口 {port} 是关闭的")


if __name__ == '__main__':
    ip = "192.168.226.20"
    ports = [80, 8080, 8081, 8082,9090,5601,8091]
    for port in ports:
        check_port(ip, port)
