#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   clean_dir.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/19 下午 9:01   hello      1.0         None

'''

import os
from datetime import datetime, timedelta

def clean_directory(directory, days):
    current_date = datetime.now()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_date= datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_date < current_date - timedelta(days=days):
                modified_date=datetime.strftime(file_date, '%Y-%m-%d %H:%M:%S')
                # os.remove(file_path)
                print (file_path,modified_date)

if __name__ == '__main__':
    directory = "D:\Download"
    days = 7
    clean_directory(directory, days)
