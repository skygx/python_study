#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   kafka-producer.py
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/18  11:27   xguo      1.0         None

'''

from kafka import KafkaProducer
import time
def main():
    producer=KafkaProducer(bootstrap_servers=["192.168.136.143:9092"])
    i=20
    while i<30:
        i+=1
        msg=f"produce:{i*2}"
        print(msg)
        producer.send("test-1",value=msg.encode('utf-8'),key=str(i).encode('utf-8'))
        time.sleep(1)
    producer.close()


if __name__ == "__main__":
    main()