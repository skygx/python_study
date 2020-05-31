#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   flatten_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/7 22:06   xguo      1.0         None

'''


def main():
    flatten = lambda x: [y for l in x for y in flatten(l)] if isinstance(x, list) else [x]
    l = [[1,2],[3,5],[4,[6,7,[8,9]]]]
    print(flatten(l))


if __name__ == "__main__":
    main()