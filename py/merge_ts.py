#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   merge_ts.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/7/26 下午 4:53   hello      1.0         None

'''

import os

filedir=r"D:\迅雷下载\aaa\download\111"

new_file=f"{filedir}\out3.ts"

f=open(new_file,'wb+')
num=490+1

for i in range(1,num):
    filepath = f"{filedir}\seg-{i}-v1-a1.ts"
    print(filepath)
    for line in open(filepath, "rb"):
        f.write(line)
    f.flush()
    os.remove(filepath)

f.close()
