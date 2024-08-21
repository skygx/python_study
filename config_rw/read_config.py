# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   read_config.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/6 上午9:56   hello      1.0         None

'''
import yaml

def add_header_footer(func):
    def wrapper(*args, **kwargs):
        print("")
        result = func(*args, **kwargs)
        print("upstream bk_svr1 {\n{} \n }"%result)
        return result
    return wrapper

def create_upstream_content(file,app,location,weight):
    with open(file, 'r') as file:
        config = yaml.safe_load(file)
    # 访问数组
    array_value = config[app][location]
    # print(array_value)
    # 原始数组
    # weight=weight
    # 要添加的字符串
    prestr=f"upstream {app} {{\n"
    substr="}"
    upstream=""
    sub_str = f" weight={weight};"

    # 使用列表推导式在每个元素前后添加字符串
    new_array = [item + sub_str for item in array_value]
    for item in new_array:
        upstream = upstream + item + "\n"
    return prestr+upstream+substr
    # my_function()
def main():
    app='c'
    location='m'
    text=create_upstream_content('ip.yaml',app,location,100)
    print(text)
    with open(f"{app}-{location}.conf",'w') as f:
        f.write(text)


if __name__ == "__main__":
    main()
