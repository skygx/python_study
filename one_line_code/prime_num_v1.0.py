#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   prime_num_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/7 21:57   xguo      1.0         None

'''


def main():
    # print(' '.join([str(item) for item in filter(lambda x:not [x%i for i in range(2,x) if x%i==0],range(2,101))]))
    print(' '.join([str(item) for item in filter(lambda x:all (map(lambda p: x%p!=0,range(2,x))),range(2,101))]))


if __name__ == "__main__":
    main()