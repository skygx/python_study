# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   productor.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/2/20 上午10:46   hello      1.0         None

'''

import pika
import faker
import time

# 随机生成数据
fake = faker.Faker()

# 无密码
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 有密码
credentials = pika.PlainCredentials("user", "password")
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.226.20',
    port=5672,  # 注意，默认为5672！5673是因为在docker初始化时设置的
    virtual_host='/',
    credentials=credentials))

channel = connection.channel()

# 创建一个队列
channel.queue_declare(queue='hello')

# 发送数据
def send_data(i):
    # 随机生成数据
    data = fake.name()
    # 发送数据
    channel.basic_publish(exchange='',
                          routing_key='hello',  # 消息队列名称
                          body=data)  # 发送的数据
    print(f" [{i}] Sent {data}")

for i in range(10000):
    send_data(i)
    time.sleep(0.1)

connection.close()
