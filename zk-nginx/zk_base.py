#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   zk_base.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/11/6 下午 12:52   hello      1.0         None

'''

from kazoo.client import KazooClient

zk=KazooClient(hosts='192.168.226.20:2181')
zk.start()
node=zk.get('/')
print(node)
zk.stop()
