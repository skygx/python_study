#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   active-code-gen.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/29  10:09   xguo      1.0         None

'''

import string
import random

class CreateString:
    def __init__(self):
        self.chars = string.ascii_letters + string.digits

    def __iter__(self):
        for _ in range(200):
            codes = []
            for _ in range(4):
                codes.append("".join(random.choices(self.chars, k=5)))

            yield "-".join(codes)


codes = CreateString()
for code in codes:
    print('code:', code)

result = "".join([x.strip("-") for x in codes])

count_tmp = {}
for k in result:
    count_tmp[k] = count_tmp.get(k, 0) + 1

print(count_tmp)

def main():
    codes = CreateString()
    for code in codes:
        print('code:', code)

    result = "".join([x.strip("-") for x in codes])

    count_tmp = {}
    for k in result:
        count_tmp[k] = count_tmp.get(k, 0) + 1

    print(count_tmp)


if __name__ == "__main__":
    main()