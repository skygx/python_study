# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   json_parse-v2.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/11/27 下午2:19   hello      1.0         None

'''

import json

# 读取 JSON 数据
with open('data.json', 'r') as f:
    json_data = f.read()

# 解析 JSON 数据
data = json.loads(json_data)
print(type(data))  # dict

for key, value in data.items():  # 遍历第一层
    print(f"Key: {key}, Value: {value}")
    # 如果值是字典，继续遍历第二层
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():  # 遍历第二层
            print(f"  Sub-key: {sub_key}, Sub-value: {sub_value}")
            # 如果第二层的值还是字典，进一步处理
            if isinstance(sub_value, dict):
                for deep_key, deep_value in sub_value.items():
                    print(f"    Deep-key: {deep_key}, Deep-value: {deep_value}")
