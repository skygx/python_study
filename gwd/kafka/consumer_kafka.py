# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   consumer_kafka.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/11/20 下午1:36   hello      1.0         None

'''
from pykafka import KafkaClient

client = KafkaClient(hosts="192.168.226.20:9092")

topic = client.topics['test']

consumer = topic.get_simple_consumer()

for message in consumer:
    print(message.offset, message.value)
