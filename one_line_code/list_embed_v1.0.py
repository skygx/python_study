#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   list_embed_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/7 22:08   xguo      1.0         None

'''


def main():
    array = lambda x: [x[i:i+3]for i in range(0,len(x),3)]
    l=[1,2,3,4,5,6,7,8,9,10]
    print(array(l))


if __name__ == "__main__":
    main()