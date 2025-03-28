# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   whoosh_write_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/12/30 上午10:19   hello      1.0         None

'''
import sqlite3
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID, DATETIME

# 创建SQLite数据库连接
conn = sqlite3.connect('whoosh_index.db')

# 定义Schema
# schema = Schema(
#     title=TEXT(stored=True),
#     content=TEXT(stored=True),
#     path=ID(stored=True)
# )
#
# # 创建Whoosh索引并存储在SQLite数据库中
# ix = create_in(conn, schema)
#
# # 添加文档
# with ix.writer() as writer:
#     writer.add_document(title="文档1", content="这是第一篇文档。", path="/a")
#     writer.add_document(title="文档2", content="这是第二篇文档。", path="/b")
#     writer.commit()  # 提交更改

schema_1 = Schema(
    title=TEXT(stored=True),
    content=TEXT(stored=True),
    path=ID(stored=True),
    date=DATETIME(stored=True)  # 日期字段
)
ix1 = create_in(conn, schema_1)

with ix1.writer() as writer:
    writer.add_document(title="文档3", content="这是第三篇文档。", path="/c", date="2021-12-31")
    writer.add_document(title="文档4", content="这是第四篇文档。", path="/d", date="2022-01-01")
    writer.commit()
