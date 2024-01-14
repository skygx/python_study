#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   prestool_demo.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/15 下午 1:50   hello      1.0         None

'''
from prestool.Tool import Tool
from icecream import ic
import inspect
import ast
tool = Tool()

def random_demo():

    name = tool.random_name() # 随机姓名
    phone = tool.random_phone()  # 随机手机号
    ssn = tool.random_ssn()  # 随机身份证

    str = tool.random_string(16)  # 随机位数的字符串
    num = tool.random_number(8)  # 随机位数的数字

    ua = tool.random_ua()  # 随机UA
    ua1 = tool.random_ua('chrome')  # 随机UA-Chrome
    ua2 = tool.random_ua('firefox')  # 随机UA-Firefox
    ua3 = tool.random_ua('ie')  # 随机UA-IE
    ua4 = tool.random_ua('opera')  # 随机UA-opera
    ua5 = tool.random_ua('safari')  # 随机UA-safari

    ic(name,phone,ssn,str,num,ua,ua1,ua2,ua3,ua4,ua5)

def main():
    ic.configureOutput(includeContext=True)
    random_demo()
    # src_ = inspect.getsource(random_demo)
    # print(src_)
    # ast_ = ast.parse(src_)
    # print(ast_)

if __name__ == '__main__':
    main()
