#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   app-1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/14  17:45   xguo      1.0         None

'''
from flask import Flask

app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__=='__main__':
    app.run()