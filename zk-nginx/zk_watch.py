#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   zk_watch.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/11/6 上午 9:24   hello      1.0         None

'''

from kazoo.client import KazooClient
import time

zk=KazooClient(hosts='192.168.226.20:2181')
zk.start()

Version=None
while True:
    @zk.DataWatch("/nginx")
    def watch_node(data,stat):
        global Version
        if Version == None:
            Version=stat
        if Version != stat:
            nginx_file=str(data,encoding='utf-8')
            print("配置已改变！！！")
            f=open('nginx.conf','w',encoding='utf-8')
            f.write(nginx_file)
            f.flush()
            f.close()
            import os
            Path=os.path.dirname(os.path.abspath(__file__))
            os.system('cp -f %s/nginx.conf /etc/nginx/nginx.conf '%Path)
        time.sleep(3)
