#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   kafka-test-consumer.py
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/18  12:12   xguo      1.0         None

'''
from kafka import KafkaConsumer
from kafka.errors import KafkaError

def main():
    try:
        consumer = KafkaConsumer("chat", bootstrap_servers=["192.168.136.143:32771"], auto_offset_reset='latest')
        for msg in consumer:
            key = msg.key.decode(encoding="utf-8")  # 因为接收到的数据时bytes类型，因此需要解码
            value = msg.value.decode(encoding="utf-8")
            print("%s-%d-%d key=%s value=%s" % (msg.topic, msg.partition, msg.offset, key, value))
    except KafkaError as e:
        print(e)
    finally:
        consumer.close()
        print('done')

if __name__ == "__main__":
    main()