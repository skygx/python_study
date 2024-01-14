#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   redis_cluster_import.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/11/29 上午 10:51   hello      1.0         None

'''

from rediscluster import RedisCluster
from faker import Faker
fake = Faker(locale='zh_CN')

# 指定配置参数

# redis_basis_conn = [{'host': '192.168.226.20', 'port': 6061}, {'host': '192.168.226.20', 'port': 6062}, {'host': '192.168.226.20', 'port': 6063}, {'host': '192.168.226.20', 'port': 6064}, {'host': '192.168.226.20', 'port': 6065}, {'host': '192.168.226.20', 'port': 6066}]
res=RedisCluster(host='192.168.226.20', port="6061", decode_responses=True)
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
