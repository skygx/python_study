# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   whoosh_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/12/30 上午9:53   hello      1.0         None

'''
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import os

# 定义一个架构
schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), path=ID(stored=True))

# 创建一个目录来存放索引
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

# 创建索引
ix = create_in("indexdir", schema)

print("Whoosh环境部署成功！")
