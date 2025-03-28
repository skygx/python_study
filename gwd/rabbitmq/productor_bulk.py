# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   productor_bulk.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/2/20 下午1:54   hello      1.0         None

'''
import pika
import json

# 连接到RabbitMQ服务器
credentials = pika.PlainCredentials("user", "password")
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.226.20',
    port=5672,  # 注意，默认为5672！5673是因为在docker初始化时设置的
    virtual_host='/',
    credentials=credentials))
channel = connection.channel()

# 确保队列存在
channel.queue_declare(queue='hello')


# 批量发送消息的函数
def send_bulk_messages(messages):
    # 开启批量发送模式
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=json.dumps(messages),
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # 设置为持久化
                          ))
    print("批量消息已发送")


# 准备一批消息
messages = [
    {"id": 1, "message": "Hello World!"},
    {"id": 2, "message": "Another message"},
    {"id": 3, "message": "Yet another message"}
]

# 发送批量消息
send_bulk_messages(messages)

# 关闭连接
connection.close()
