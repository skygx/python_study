#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   kafka-test-producer.py
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/18  11:27   xguo      1.0         None

'''

from kafka import KafkaProducer
from kafka.errors import KafkaError
import time
import random


def main():

    try:
        producer = KafkaProducer(bootstrap_servers=["192.168.136.110:9093","192.168.136.110:9094","192.168.136.110:9095"])
        # producer = KafkaProducer(brokers=["192.168.136.143:9092"])
        i = 1
        while i < 30:
            i+=1
            r = random.randint(1, 100)
            msg=f"test:{r}"
            print(msg)
            producer.send("test",value=msg.encode('utf-8'),key=str(i).encode('utf-8'))
            time.sleep(1)
    except KafkaError as e:
        print(e)
    finally:
        # producer.close()
        print('done!!!')



if __name__ == "__main__":
    main()