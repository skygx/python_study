#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   dns_cname.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/21 下午 4:09   hello      1.0         None

'''

import dns.resolver

domain = input('Please input an domain: ')
try:
    cname = dns.resolver.resolve(domain, "CNAME")
    for rdata in cname:
        print(f'{domain}: {rdata.target}')
except dns.resolver.NoAnswer:
    print(f'{domain}: No answer')


