# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   monitor_file.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/30 上午10:24   hello      1.0         None

'''
import time
import os
import hashlib
def get_file_hash(filename):
    hasher = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

if __name__ == '__main__':
    last_hash = None
    while True:
        current_hash = get_file_hash('test.txt')
        if current_hash != last_hash:
            print("File has changed!")
        last_hash = current_hash
        time.sleep(1)
