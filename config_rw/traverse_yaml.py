# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   traverse_yaml.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/7 上午10:04   hello      1.0         None

'''

import yaml

# 假设有一个名为example.yaml的文件
yaml_file = 'ip.yaml'

# 使用yaml.safe_load()读取YAML文件内容
with open(yaml_file, 'r') as file:
    data = yaml.safe_load(file)


# 遍历YAML文件中的数据
def traverse(data, parent_key=None):
    if isinstance(data, dict):
        for key in data:
            traverse(data[key], parent_key=key)
    elif isinstance(data, list):
        for item in data:
            traverse(item, parent_key)
    else:
        print(f"{'  ' * (parent_key is not None)}{parent_key}: {data}")


traverse(data)
