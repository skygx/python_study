#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   flask_cache_test1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/22 下午 2:39   hello      1.0         None

'''
from flask import Flask
from flask_caching import Cache
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'skyccc'

cache = Cache(app, config={'CACHE_TYPE': 'redis',
                           'CACHE_REDIS_HOST': '192.168.226.20',
                           'CACHE_REDIS_PORT': 6380,
                           'CACHE_REDIS_DB': 0,
                           'CACHE_REDIS_PASSWORD': 'admin',
                           'CACHE_REDIS_URL': 'redis://:admin@192.168.226.20:6380/0'})

@app.route('/')
def home():
    # 缓存函数的返回值，缓存键为'home_page'
    @cache.cached(timeout=100, key_prefix='cc')
    def get_home_page():
        time.sleep(3)
        return "Hello, World!"

    return get_home_page()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
