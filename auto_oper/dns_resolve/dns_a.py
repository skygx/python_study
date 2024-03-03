#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   dns_a.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/21 下午 4:02   hello      1.0         None

'''
import dns.resolver

domain = input('Please input an domain: ')
A = dns.resolver.resolve(domain, "A")
for i in A.response.answer:
    for j in i.items:
        if j.rdtype == 1:
            print(j.address)
