#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   zk_nginx.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/11/6 下午 12:58   hello      1.0         None

'''

from kazoo.client import KazooClient
import time
zk=KazooClient(hosts='192.168.226.20:2181')
zk.start()
config_file='/etc/nginx/nginx.conf20231106'

with open(config_file,'r') as f:
    nginx_config=f.readlines()
print nginx_config
#zk.set('/nginx',bytes(nginx_config,encoding='utf-8'))
zk.set('/nginx',bytes(nginx_config))
zk.stop()
