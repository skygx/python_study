#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   diff_file_line.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/4/4 上午 11:24   hello      1.0         None

'''
import difflib

with open('db.properties', 'r') as f1, open('db1.properties', 'r') as f2:
    diff = difflib.ndiff(f1.readlines(), f2.readlines())
    diff_list = list(diff)

for line in diff_list:
    if line.startswith('+'):
        print(f'新增行：{line}')
    elif line.startswith('-'):
        print(f'删除行：{line}')
    elif line.startswith('?'):
        print(f'修改行：{line}')
    else:
        print(f'相同行：{line}')
