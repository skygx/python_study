# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   whoosh_file.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/12/30 上午10:20   hello      1.0         None

'''
from whoosh.writing import IndexWriter
import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID, DATETIME
import datetime

# 定义一个架构
schema = Schema(
    title=TEXT(stored=True),    # 存储文档标题
    content=TEXT(stored=True),  # 存储文档内容
    path=ID(stored=True)        # 存储文档路径
)

# 创建一个目录来存放索引
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

# 创建索引
# ix = create_in("indexdir", schema)
#
# writer = ix.writer()  # 创建写入器
# writer.add_document(title="First document", content="This is the content of the first document.", path="/a")
# writer.add_document(title="Second document", content="This is the content of the second document.", path="/b")
# # writer.commit()  # 提交更改
# writer.update_document(path="/a", title="Updated document title", content="Updated content.")
#
#
# writer.delete_by_term('path', '/b')
# writer.commit()

schema_1 = Schema(
    title=TEXT(stored=True),
    content=TEXT(stored=True),
    path=ID(stored=True),
    date=DATETIME(stored=True)  # 日期字段
)

ix1 = create_in("indexdir", schema_1)

writer1 = ix1.writer()
writer1.add_document(title="First document", content="This is the content of the first document.", path="/a", date=datetime.datetime(2024, 12, 31))
writer1.add_document(title="Second document", content="This is the content of the second document.", path="/b",date=datetime.datetime(2024, 12, 30))
# writer.commit()  # 提交更改
writer1.update_document(path="/a", title="Updated document title", content="Updated content.")
writer1.add_document(title="Third document", content="This is the content of the third document.", path="/c", date=datetime.datetime.now())
writer1.add_document(title="Fourth document", content="This is the content of the fourth document.", path="/d", date=datetime.datetime(2024, 12, 31))
writer1.commit()
