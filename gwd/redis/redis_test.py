# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   redis_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/12/17 下午4:12   hello      1.0         None

'''

import redis

# 创建redis连接
r = redis.Redis(host='192.168.226.20', port=16380, db=0, password='123456')

# 设置键值对
r.set('name', 'hello')

# 获取键值对
print(r.get('name'))
