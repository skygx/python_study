# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   cluster_productor.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/2/25 下午1:47   hello      1.0         None

'''
import pika

# 定义RabbitMQ集群的节点地址
nodes = ['amqp://user:password@192.168.226.20:5672', 'amqp://user:password@192.168.226.20:5673', 'amqp://user:password@192.168.226.20:5674']

# 使用pika的ConnectionParameters指定多个节点
parameters = pika.ConnectionParameters(connection_attempts=3, retries=1, backoff_policy=lambda x: x * 2,
                                       socket_timeout=5,
                                       credentials=pika.PlainCredentials('user', 'password'),
                                       hostnames=nodes)

# 建立连接
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# 声明一个队列
channel.queue_declare(queue='hello')

# 发送消息
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

# 关闭连接
connection.close()
