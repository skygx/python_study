#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   random_str.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/18  10:07   xguo      1.0         None

'''

import random

def ranstr(num):
    # 猜猜变量名为啥叫 H
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    F = '~!@#$%^&*()_+=-{}[]<>?/:;|'

    salt = ''
    for i in range(num):
        salt += random.choice(H+F)
    return salt



def main():
    salt = ranstr(10)
    print(salt)

if __name__ == "__main__":
    main()