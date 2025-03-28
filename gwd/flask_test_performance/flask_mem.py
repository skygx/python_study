# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   flask_mem.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/13 上午10:21   hello      1.0         None

'''
from flask import Flask
import time
import os
import gc
import psutil

app = Flask(__name__)

# 全局变量用于存储不断增加的数据
data = []

@app.route('/')
def memory_leak():
    # memory_info = psutil.virtual_memory()
    # swap_info = psutil.swap_memory()
    #
    # # 返回内存和swap占用信息
    # return (f"Memory Usage: {memory_info.used / 1024 / 1024:.2f} MB / {memory_info.total / 1024 / 1024:.2f} MB\n"
    #         f"Swap Usage: {swap_info.used / 1024 / 1024:.2f} MB / {swap_info.total / 1024 / 1024:.2f} MB")
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    swap_info = psutil.swap_memory()

    # 返回当前程序的内存和swap占用信息
    return (f"Memory Usage: {memory_info.rss / 1024 / 1024:.2f} MB\n"
            f"Swap Usage: {swap_info.used / 1024 / 1024:.2f} MB / {swap_info.total / 1024 / 1024:.2f} MB")
@app.route('/get_memory')
def memory_usage():
    # 获取当前内存使用情况
    memory_info = psutil.Process(os.getpid()).memory_info()
    return f"Memory usage: {memory_info.rss / 1024 / 1024:.2f} MB"

@app.route('/cleanup')
def cleanup_memory():
    # 手动触发垃圾回收
    gc.collect()
    data.clear()
    return "Memory cleanup triggered."

@app.route('/add_mem')
def add_memory():
    global data
    # 增加1GB内存
    data.append(' ' * 1024 * 1024 * 1024)  # 1GB
    memory_info = psutil.Process(os.getpid()).memory_info()
    return f"Added 1GB of memory. Current memory usage: {memory_info.rss / 1024 / 1024:.2f} MB"

@app.route('/drop_mem')
def drop_memory():
    global data
    # 释放内存
    data.clear()
    gc.collect()  # 手动触发垃圾回收
    memory_info = psutil.Process(os.getpid()).memory_info()
    return f"Memory dropped. Current memory usage: {memory_info.rss / 1024 / 1024:.2f} MB"


if __name__ == '__main__':
    app.run(debug=True)
