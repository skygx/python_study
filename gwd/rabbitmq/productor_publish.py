# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   prod_publish.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/2/21 上午10:16   hello      1.0         None

'''

import pika

# 无密码
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 有密码
credentials = pika.PlainCredentials("user", "password")
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.226.20',
    port=5672,
    credentials=credentials))

channel = connection.channel()

# 设置订阅模式
channel.exchange_declare(exchange='s1', durable=True, exchange_type='fanout')
# 创建一个队列
# channel.queue_declare(queue='hello',durable=True)

# 发送数据
channel.basic_publish(exchange='s1',
                      routing_key='',  # 消息队列名称
                      body='Hello World!',  # 发送的数据
                      )
print(" [x] Sent 'Hello World!'")

connection.close()
