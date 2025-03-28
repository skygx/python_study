# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   find_bigsize.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/30 上午9:11   hello      1.0         None

'''
import os
for root, dirs, files in os.walk('.'):
    for name in files:
        if os.path.getsize(os.path.join(root, name)) > 1024 * 1024:  # 大于1MB
            print(os.path.join(root, name))
