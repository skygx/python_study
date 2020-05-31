#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   FizzBuzz.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/7 21:23   xguo      1.0         None

'''


def main():
    for x in range(1,101):print("fizz"[x%3*4:]+"buzz"[x%5*4:]or x)


if __name__ == "__main__":
    main()