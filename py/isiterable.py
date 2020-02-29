#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   isiterable.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/8  10:41   xguo      1.0         None

'''


def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False

def main():
    params = [
        1234,
        '1234',
        [1, 2, 3, 4],
        set([1, 2, 3, 4]),
        {1: 1, 2: 2, 3: 3, 4: 4},
        (1, 2, 3, 4)
    ]

    for param in params:
        print('{} is iterable? {}'.format(param, is_iterable(param)))


if __name__ == "__main__":
    main()