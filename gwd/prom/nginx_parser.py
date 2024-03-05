#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   nginx_parser.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/11/15 上午 8:40   hello      1.0         None

'''

from nginxparser_eb import load
import pprint

tree = load(open('/etc/nginx/nginx.conf','r'))

# parsed_config = parse_config(tree)
# print parsed_config

# print tree
pprint.pprint(tree)
