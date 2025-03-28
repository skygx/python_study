# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   flask_lock.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/13 上午9:42   hello      1.0         None

'''
from flask import Flask
import threading

app = Flask(__name__)

# 创建一个锁对象
lock = threading.Lock()

@app.route('/')
def locked_response():
    # 获取锁，模拟锁死的情况
    lock.acquire()
    print('Locked')
    # try:
    #     # 这里模拟一个永远不会释放锁的操作
    #     while True:
    #         pass
    # finally:
    #     # 理论上应该释放锁，但这里永远不会执行
    #     lock.release()
    return 'Locked'

@app.route('/unlock')
def unlock():
    # 释放锁
    lock.release()
    print('Unlocked')
    return 'Unlocked'

if __name__ == '__main__':
    app.run(debug=True)
