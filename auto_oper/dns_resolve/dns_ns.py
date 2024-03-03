#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   dns_ms.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/21 下午 4:04   hello      1.0         None

'''
import dns.resolver

domain = input('Please input an domain: ')
ns = dns.resolver.resolve(domain, "NS")
for i in ns.response.answer:
    for j in i.items:
        print(j.to_text())
