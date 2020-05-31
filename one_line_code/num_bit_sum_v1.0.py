#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   num_bit_sum_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/7 22:10   xguo      1.0         None

'''


def main():
    bitsum = lambda x:sum(map(int,str(x**100)))
    print(2**1000)
    print(bitsum(2))


if __name__ == "__main__":
    main()