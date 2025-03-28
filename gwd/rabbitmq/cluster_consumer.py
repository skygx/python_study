# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   cluster_consumer.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/2/25 下午1:49   hello      1.0         None

'''
import pika

# 定义RabbitMQ集群的节点地址
nodes = ['amqp://user:password@192.168.226.20:5672', 'amqp://user:password@192.168.226.20:5673', 'amqp://user:password@192.168.226.20:5674']

# 使用pika的ConnectionParameters指定多个节点
parameters = pika.ConnectionParameters(connection_attempts=3,
                                       socket_timeout=5,
                                       credentials=pika.PlainCredentials('user', 'password'),
                                       host=nodes)

# 建立连接
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

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
