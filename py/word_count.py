#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   word_count.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/6  13:56   xguo      1.0         None

'''


def main():
    str = 'helloworld'
    c = {}
    for i in str:
        c[i] = c.get(i,0) + 1
    print(c)

if __name__ == "__main__":
    main()