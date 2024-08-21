# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   panel_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/5/20 上午10:46   hello      1.0         None

'''
import panel as pn

pn.extension()
title = pn.panel("# Hello, Panel!")
text = pn.panel("Welcome to the exciting world of Panel.")
pn.Column(title, text).show()
