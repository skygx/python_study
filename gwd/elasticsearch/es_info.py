# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   es_info.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/11/20 下午4:09   hello      1.0         None

'''
from elasticsearch import Elasticsearch
from pprint import pprint

# 连接到Elasticsearch服务
es = Elasticsearch(["http://elastic:elastic@192.168.226.20:9200"])

# 如果Elasticsearch服务需要认证，可以这样设置
# es = Elasticsearch(["http://username:password@localhost:9200"])
pprint(es.info())
