# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   purge_queue.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/2/20 下午2:36   hello      1.0         None

'''
import pika

credentials = pika.PlainCredentials("user", "password")
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.226.20',
    port=5672,  # 注意，默认为5672！5673是因为在docker初始化时设置的
    virtual_host='/',
    credentials=credentials))

channel = connection.channel()

channel.queue_purge('hello')
connection.close()
