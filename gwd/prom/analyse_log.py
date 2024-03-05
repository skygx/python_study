#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   analyse_log.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/5 上午 9:48   hello      1.0         None

'''

import re

with open('log.txt', 'r') as f:
    log = f.read()
pattern = re.compile(r'ERROR:\s+(.*)', flags=re.IGNORECASE)
errors = pattern.findall(log)

for error in errors:
    print(error)
