#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   setup.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/21 下午 6:38   hello      1.0         None

'''

# setup.py(hello.py 的同目录下，必须以这个命名)
from setuptools import setup

setup(
 name='hello',
 version='0.1',
 py_modules=['hello'],
 install_requires=[
 'Click',
 ],
 entry_points='''
 [console_scripts]
 hello=hello:add
 '''
)
