# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   import_kafka.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/5/28 下午1:55   hello      1.0         None

'''
from pykafka import KafkaClient

client = KafkaClient(hosts="192.168.226.20:9092")

topic = client.topics['my_topic']

with topic.get_sync_producer() as producer:
    for i in range(10000):
        producer.produce(('test message ' + str(i)).encode())
