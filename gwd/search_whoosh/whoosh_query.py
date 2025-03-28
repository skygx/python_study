# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   whoosh_query.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/12/30 上午10:23   hello      1.0         None

'''
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh.query import Or, And
from whoosh.highlight import UppercaseFormatter
from whoosh.fields import DATETIME, TEXT, ID, Schema
from whoosh.scoring import WeightingModel
from whoosh.query import DateRange
from whoosh.qparser import QueryParser
import datetime

# 打开已有索引
ix = open_dir("indexdir")

# 创建搜索器
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("first")
    results = searcher.search(query)
    for result in results:
        print(result['title'], result['path'])

query = Or([
    QueryParser("content", ix.schema).parse("first"),
    QueryParser("content", ix.schema).parse("second")
])

with ix.searcher() as searcher:
    results = searcher.search(query)
    for result in results:
        print(result['title'], result['path'])

query = QueryParser("content", ix.schema).parse('"first document"')

with ix.searcher() as searcher:
    results = searcher.search(query)
    for result in results:
        print(result['title'], result['path'])

with ix.searcher() as searcher:
    results = searcher.search(query, sortedby="title")  # 按照标题排序
    for result in results:
        print(result['title'], result['path'])

with ix.searcher() as searcher:
    results = searcher.search(query)
    for result in results:
        title = result.highlights("title")
        content = result.highlights("content")
        print(f"Title: {title}\nContent: {content}\n")

with ix.searcher() as searcher:
    results = searcher.search(query, limit=3)  # 第21到第30个结果
    for result in results:
        print(result['title'], result['path'])
        print(result)

# 在Schema中添加DATETIME字段
schema_1 = Schema(
    title=TEXT(stored=True),
    content=TEXT(stored=True),
    path=ID(stored=True),
    date=DATETIME(stored=True)  # 日期字段
)

start_date = datetime.datetime(2024, 1, 1)
end_date = datetime.datetime(2024, 12, 31)
# 范围查询示例
date_query = DateRange("date", start_date, end_date)

with ix.searcher() as searcher:
    results = searcher.search(date_query)
    print("日期范围查询结果:")
    for result in results:
        print(result['title'], result['path'])

query_string = "third AND document"
query = QueryParser("content", ix.schema).parse(query_string)

with ix.searcher() as searcher:
    results = searcher.search(query)
    print("查询解析器结果:")
    for result in results:
        print(result['title'], result['path'])

query = QueryParser("content", ix.schema).parse("first")

#评分
with ix.searcher() as searcher:
    results = searcher.search(query)
    for result in results:
        print(f"Title: {result['title']}, Score: {result.score}")

#排序
with ix.searcher() as searcher:
    results = searcher.search(query, sortedby="title")  # 按照标题排序
    for result in results:
        print(result['title'], result['path'])


with ix.searcher() as searcher:
    results = searcher.search(query, sortedby=None)  # 默认按评分排序
    for result in results:
        print(f"Title: {result['title']}, Score: {result.score}")


