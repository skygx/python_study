#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   dns_mx.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/21 下午 4:04   hello      1.0         None

'''
import dns.resolver

domain = input('Please input an domain: ')
MX = dns.resolver.resolve(domain, "MX")
for i in MX:
    print("MX preference = ", i.preference, 'mail exchanger = ', i.exchange)
