# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   batch_rename.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/30 上午9:05   hello      1.0         None

'''
import os
for filename in os.listdir('.'):
    os.rename(filename, filename.replace('log', 'txt'))
