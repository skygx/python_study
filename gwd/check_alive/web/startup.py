# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   startup.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/26 下午4:14   hello      1.0         None

'''
from gevent import pywsgi
from url_health import app

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 8080), app)
    server.serve_forever()
