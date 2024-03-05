#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   get_ip.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/4 上午 8:55   hello      1.0         None

'''

import requests
import time

def get_public_ip():
    response = requests.get('https://httpbin.org/ip')
    ip_info = response.json()
    return ip_info['origin']

def get_city_from_ip(ip):
    url = f'http://ip-api.com/json/{ip}?fields=city'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('city', '未知城市')
    else:
        return '无法获取城市信息'

if __name__ == '__main__':
    public_ip = get_public_ip()
    print(f'公网IP: {public_ip}')
    city = get_city_from_ip(public_ip)
    print(f'城市: {city}')
    # while True:
    #     time.sleep(1)
