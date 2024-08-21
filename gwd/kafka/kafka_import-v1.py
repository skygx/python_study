# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   kafka_import-v1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/5/28 下午2:14   hello      1.0         None

'''

from kafka import KafkaProducer
import json

# 配置Kafka生产者
# producer = KafkaProducer(bootstrap_servers=['192.168.226.20:9092'],
#                          value_serializer=lambda m: json.dumps(m).encode('utf-8'))
producer = KafkaProducer(bootstrap_servers='192.168.226.20:9092')
# 创建一条消息
message = {"id": 1, "msg": "Hello, Kafka!"}

# 发送消息到Kafka的'test'主题
#producer.send('my_topic', message)
producer.send('my_topic', b'hello, kafka!')

# 确保所有消息都被发送
producer.flush()

producer.close()
