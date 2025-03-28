# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   rocketmq_product.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/19 上午9:47   hello      1.0         None

'''
from rocketmq.client import Producer, Message

# 初始化生产者
producer = Producer('ProducerGroupName')
producer.set_namesrv_addr('192.168.226.20:9876')  # 设置NameServer地址
producer.start()

# 创建消息
msg = Message('TestTopic', 'TagA', 'Hello RocketMQ'.encode('utf-8'))

# 发送消息
ret = producer.send_sync(msg)
print(f"Send message status: {ret.status}")

# 关闭生产者
producer.shutdown()

