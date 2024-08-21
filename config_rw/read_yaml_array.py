# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   read_yaml_array.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/7 上午9:56   hello      1.0         None

'''


import yaml
import pprint

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return list(yaml.safe_load_all(f.read()))


data = read_yaml("ip.yaml")
pprint.pprint(data)


