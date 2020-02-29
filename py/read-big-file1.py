#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   read-big-file1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/29  20:12   xguo      1.0         None

'''

def python_read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                return
            yield line


def main():
    g = python_read('big-file.txt')
    for c in g:
        print(c,end='')


if __name__ == "__main__":
    main()