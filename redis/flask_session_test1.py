#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   flask_session_test1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/22 下午 4:01   hello      1.0         None

'''

from flask import Flask, session
from redis import Redis
from flask_session import Session

app = Flask(__name__)
app.debug = True
app.secret_key = 'your secret key here'

# 配置Session以使用Redis
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host='192.168.226.20', port=6380, password='admin',db=0)
Session(app)


@app.route('/')
def index():
    # 使用session
    session['key'] = 'value'
    return 'Session stored in Redis'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
