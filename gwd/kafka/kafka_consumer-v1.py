# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   kafka_consumer-v1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/5/28 下午3:01   hello      1.0         None

'''
from kafka import KafkaConsumer

# 要消费的Kafka主题
topic = 'my_topic'

# Kafka消费者实例
consumer = KafkaConsumer(topic, bootstrap_servers=['192.168.226.20:9092'])

# 循环获取消息
for message in consumer:
    # 打印消息
    print(message.value.decode('utf-8'))
