# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   consumer.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/2/20 上午10:50   hello      1.0         None

'''

import pika

credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.226.20',
    port=5672,
    virtual_host='/',
    credentials=credentials))

channel = connection.channel()

# 申明消息队列，消息在这个队列传递，如果不存在，则创建队列
channel.queue_declare(queue='hello')


# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    print(f"消费者接收到了任务: {body.decode()}")


# 告诉rabbitmq，用callback来接收消息
channel.basic_consume(
    queue='hello',
    auto_ack=True,
    on_message_callback=callback
)

# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
channel.start_consuming()
