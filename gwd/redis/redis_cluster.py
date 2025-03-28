# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   redis_cluster.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/12/19 上午10:51   hello      1.0         None

'''
from rediscluster import RedisCluster

startup_nodes = [
    {'host': '192.168.226.20', 'port': '6061'},
    {'host': '192.168.226.20', 'port': '6062'},
    {'host': '192.168.226.20', 'port': '6063'},
    {'host': '192.168.226.20', 'port': '6064'},
    {'host': '192.168.226.20', 'port': '6065'},
    {'host': '192.168.226.20', 'port': '6066'}
]

redis_cluster = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

# redis_cluster.set('name', 'hello')
# print(redis_cluster.get('name'))
#
# redis_cluster.set('age', 25)
# print(redis_cluster.get('age'))
#
# redis_cluster.set('city', 'beijing')
# print(redis_cluster.get('city'))

# print(redis_cluster.dbsize())
# print(redis_cluster.keys())
# print(len(redis_cluster.keys()))
# print(redis_cluster.scan())
# redis_cluster.hmset('user:1', {'name': 'hello', 'age': 25, 'city': 'beijing'})
# redis_cluster.hmset("user:2", {'name': 'world', 'age': 30, 'city': 'hangzhou'})
# redis_cluster.hmset("user:3", {'name': 'gwd', 'age': 28, 'city': 'guangzhou'})
# redis_cluster.hmset("user:4", {'name': 'xguo', 'age': 35, 'city': 'wuhan'})
# redis_cluster.hmset("user:5", {'name': 'guoxin_well', 'age': 26, 'city': 'beijing'})
# print(redis_cluster.hgetall("""user:1"""))
# 示例：使用SCAN命令遍历所有键（注意：这是一个迭代器，需要循环遍历）

# count = count_set_keys(redis_cluster)
# print(f"string count: {count}")
def count_keys(redis_cluster):
    string_count=0
    hash_count=0
    list_count=0
    set_count=0
    zset_count=0
    cursor='0'
    count={}


    # keys=redis_cluster.scan(cursor=cursor, match='*', count=1000)
    keys=redis_cluster.scan_iter(match='*', count=1000)
    for k in keys:
        # print(key)

    # for key in keys:
    #     for k in keys[key][1]:
            # print(redis_cluster.type(k))
        if redis_cluster.type(k) == 'string':
            string_count+=1
        elif redis_cluster.type(k) == 'hash':
            # print(k)
            hash_count+=1
        elif redis_cluster.type(k) == 'list':
            list_count+=1
        elif redis_cluster.type(k) == 'set':
            set_count+=1
        elif redis_cluster.type(k) == 'zset':
            zset_count+=1
        else:
            print("unknown type")

    count['string']=string_count
    count['hash']=hash_count
    count['list']=list_count
    count['set']=set_count
    count['zset']=zset_count
    return count

count=count_keys(redis_cluster)
print(count)

        # print(keys[key][i],keys[key][i+1])

