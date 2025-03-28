# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   productor_direct.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/2/21 下午2:54   hello      1.0         None

'''
import pika

credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.226.20', port=5672, virtual_host='/', credentials=credentials))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
channel.basic_publish(exchange='direct_logs', routing_key='info', body='Info: Hello World!')
connection.close()
