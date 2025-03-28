# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   json_parse.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/11/27 上午8:48   hello      1.0         None

'''
import json

def json_parse(json_str):
    json_obj = json.loads(json_str)
    print(type(json_obj))

    with open("./test.txt","w") as f:
        for item in json_obj:
            f.write(item['original_md5'] + " " + item['name'] + "\n")

def main():
    with open("./test.json","r") as f:
        json_str = f.read()
    json_parse(json_str)

if __name__ == '__main__':
    main()
