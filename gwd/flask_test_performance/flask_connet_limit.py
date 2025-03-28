#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   flask_connet_limit.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/2/27 上午11:07   hello      1.0         None

'''
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import time
import random

app = Flask(__name__)

# 初始化 Limiter
limiter = Limiter(
    get_remote_address,  # 根据客户端 IP 地址进行限制
    app=app,
    default_limits=["200 per day", "50 per hour"]  # 全局默认限制
)

# 限制某个 URL 的连接数
@app.route("/limited")
@limiter.limit("5 per minute")  # 每分钟最多 10 次请求
def limited_route():
    time.sleep(random.randint(1, 10))  # 模拟延迟
    return "This route is rate-limited!"

@app.route("/unlimited")
def unlimited_route():
    return "This route is not rate-limited!"

if __name__ == "__main__":
    app.run(debug=True)
