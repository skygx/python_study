#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   get_localip.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/10 下午 2:08   hello      1.0         None

'''
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("本机名称为：" + hostname)
print("本机的IP地址为：" + IPAddr)
