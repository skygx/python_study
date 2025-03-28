# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   rocketmq_consumer.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/19 上午9:49   hello      1.0         None

'''
from rocketmq.client import PushConsumer, ConsumeStatus
import time
# 定义消息处理函数
def on_message(msg):
    print(f"Received message: {msg.di} {msg.body.decode('utf-8')}")
    return ConsumeStatus.CONSUME_SUCCESS

# 初始化消费者
consumer = PushConsumer('ConsumerGroupName')
consumer.set_name_server_address('192.168.226.20:9876')  # 设置NameServer地址
consumer.subscribe('TestTopic', on_message)


# 启动消费者
consumer.start()

while True:
    time.sleep(180)

# 关闭消费者
consumer.shutdown()
