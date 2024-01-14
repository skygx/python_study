#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   import_redis_datas.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/11/29 上午 10:42   hello      1.0         None

'''
import redis
import rediscluster
from faker import Faker
fake = Faker(locale='zh_CN')

# 指定配置参数

res = redis.Redis(host='192.168.226.20', port=6380, db=0,password="admin")

if not res:
    print("连接redis集群失败")
else:
    print("连接redis集群成功")
# 创建文件变量

fileName = "sampleData.txt"

# 打开文件，并遍历文件中的每一行

i=0

with open(fileName, "r", encoding="utf-8") as f:
    for line in f:
        # 将每一行数据存储在Redis中
        # print(line.strip(),line)
        res.set(line.strip(), fake.pystr(min_chars=3, max_chars=8))
        i=i+1
print(i)
