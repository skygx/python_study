#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   json_read.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/26  10:59   xguo      1.0         None

'''
import json
import os

def main():
    for f in os.listdir('../txt'):
        print(f)
    with open('../txt/k8s-master', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        # print(json_data)
    print(json_data.get('ansible_facts').get('ansible_all_ipv4_addresses'))

if __name__ == "__main__":
    main()