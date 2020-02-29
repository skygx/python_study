#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   read_big_file.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/29  20:01   xguo      1.0         None

'''

import pandas as pd

def pandas_read(filename, sep=',',chunksize=5):
    reader = pd.read_csv(filename, sep, chunksize=chunksize)
    while True:
        try:
            yield reader.get_chunk()
        except StopIteration:
            print('---Done---')
            break


def main():
    g = pandas_read('big-file.txt',sep='\n')
    for c in g:
        print(c)


if __name__ == "__main__":
    main()