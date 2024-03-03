#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   hello.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/21 下午 6:35   hello      1.0         None

'''
#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import click

@click.command()
@click.option('-user', prompt='请输入名字', help='增加用户')
def add(user):
 """增加用户"""
 click.echo('add user: %s' % user)

