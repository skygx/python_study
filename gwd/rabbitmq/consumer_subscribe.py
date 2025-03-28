# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   consumer_subscribe.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/2/21 上午10:18   hello      1.0         None

'''
import pika

credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.226.20',
    port=5672,
    virtual_host='/',
    credentials=credentials))

channel = connection.channel()

# 设置订阅模式
channel.exchange_declare(exchange='s1', durable=True, exchange_type='fanout')
# 随机生成队列
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
print(queue_name)
# 绑定 exchange 和 queue 绑定
channel.queue_bind(exchange='s1', queue=queue_name)


# 申明消息队列，消息在这个队列传递，如果不存在，则创建队列
# channel.queue_declare(queue = 'hello')

# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f"消费者接收到了任务: {body.decode()}")


# 闲置消费
channel.basic_qos(prefetch_count=1)

# 告诉rabbitmq，用callback来接收消息
channel.basic_consume(
    # queue='m1',
    queue=queue_name,
    auto_ack=False,
    on_message_callback=callback
)

# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
channel.start_consuming()
