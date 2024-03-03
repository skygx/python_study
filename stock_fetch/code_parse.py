#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   code_parse.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/3 下午 6:55   hello      1.0         None

'''

import json
import pprint

def parse_code():
    codes={}
    with open('./rates_code.json','r',encoding='utf-8') as f:
        r = json.load(f)
    for i in r:
        code = i['code']
        name = i['name']
        codes[code] = name
    return codes


if __name__ == '__main__':
    codes = parse_code()
    pprint.pprint(codes)
