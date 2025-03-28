# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   redis_sentinel.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/12/18 下午1:27   hello      1.0         None

'''
from redis.sentinel import Sentinel

# Sentinel服务地址列表
sentinel_services = [
    ('192.168.226.20', 26379),
    ('192.168.226.20', 26380),
    ('192.168.226.20', 26381)
]

# 初始化Sentinel对象
sentinel = Sentinel(sentinel_services, socket_timeout=0.5)

data = sentinel.discover_master('mymaster')
print(data)

# 获取主服务器中的一个Redis实例
master = sentinel.master_for('mymaster', socket_timeout=0.5, password='123456', db=0)

# 获取从服务器中的一个Redis实例
slave = sentinel.slave_for('mymaster', socket_timeout=0.5, password='123456',db=0)

# print(master)
# print(slave)
# # 使用master实例进行操作
master.set('test', 'hello')
master.hset('test_hash', 'name', 'guoxin_well')
master.hset('test_hash','age', 26)
# # 使用slave实例进行读操作
# value = slave.get('test')
value = master.hget('test_hash', 'age')
print(value)

# 断开连接
master.close()
slave.close()
