# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   random_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/30 上午10:28   hello      1.0         None

'''
import random
import string

if __name__ == '__main__':
    random_number = random.randint(1, 100)
    print(random_number)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    print(random_string)
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    print(password)
