#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   sync_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/1/12 下午 2:29   hello      1.0         None

'''
from flask import Flask, request

app = Flask(__name__)


@app.route('/file')
def file():
    with open("demo.txt") as f:
        text = f.read()
    return text


if __name__ == '__main__':
    app.run(port=8090, host="0.0.0.0")
