# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   flask_net_wait.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/14 上午9:40   hello      1.0         None

'''
from flask import Flask
import socket
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Flask app. Visit /close to simulate CLOSE_WAIT or /time to simulate TIME_WAIT."

@app.route('/close')
def close_wait():
    # 模拟CLOSE_WAIT状态
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 5000))  # 连接到自身
    s.send(b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n')
    time.sleep(10)  # 保持连接打开，模拟CLOSE_WAIT
    s.close()
    return "Simulated CLOSE_WAIT connection."

@app.route('/time')
def time_wait():
    # 模拟TIME_WAIT状态
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 5000))  # 连接到自身
    s.send(b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n')
    s.close()  # 关闭连接，进入TIME_WAIT状态
    return "Simulated TIME_WAIT connection."

@app.route('/sent')
def syn_sent():
    # 模拟SYN_SENT状态
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('127.0.0.1', 5000))  # 尝试连接到自身
    except ConnectionRefusedError:
        pass  # 连接被拒绝，模拟SYN_SENT状态
    return "Simulated SYN_SENT connection."

@app.route('/recv')
def syn_recv():
    # 模拟SYN_RECV状态
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 5001))  # 绑定到另一个端口
    s.listen(1)  # 监听连接
    s.accept()  # 接受连接，模拟SYN_RECV状态
    return "Simulated SYN_RECV connection."

@app.route('/fin')
def fin_wait():
    # 模拟FIN_WAIT状态
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 5000))  # 连接到自身
    s.send(b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n')
    s.shutdown(socket.SHUT_WR)  # 关闭写端，模拟FIN_WAIT状态
    time.sleep(10)  # 保持连接打开，模拟FIN_WAIT
    s.close()
    return "Simulated FIN_WAIT connection."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
