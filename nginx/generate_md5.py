#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   generate_md5.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/1/29 上午 9:09   hello      1.0         None

'''

import hashlib
print(hashlib.md5(b'index.htmlmySecret').hexdigest())
# 'a53bee08a4bf0bbea978ddf736363a12'
