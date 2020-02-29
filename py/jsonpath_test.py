#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   jsonpath.py
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/3 14:45   xguo      1.0         None

'''
import json
import jsonpath

def main():
    jsonObj = json.load(open(r'json_file.json','r'))

    index = jsonpath.jsonpath(jsonObj, '$.hits.total')
    print(index)


if __name__ == "__main__":
    main()