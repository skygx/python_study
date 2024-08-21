#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   fake_request.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/19 下午 2:49   hello      1.0         None

'''
import requests
from faker import Faker
url = "http://192.168.226.20"
fake = Faker()

for i in range(10):
    ip_addr = fake.ipv4()
    headers = {"Client-IP": ip_addr, "X-Forwarded-For": ip_addr}
    req=requests.get(url,headers=headers, verify=False)
    # print(req.status_code)
    print(ip_addr)
