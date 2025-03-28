# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   flask_cpu.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/14 上午9:21   hello      1.0         None

'''
from flask import Flask
import time
import psutil
import multiprocessing

app = Flask(__name__)
processes = []

def consume_cpu():
    # 无限循环占用CPU
    while True:
        pass
@app.route('/')
def index():
    return "Welcome to the Flask app. Visit /increase_cpu to increase CPU usage or /decrease_cpu to lower CPU usage."

@app.route('/increase_cpu')
def increase_cpu():
    global processes

    # 获取CPU核心数
    num_cores = multiprocessing.cpu_count()

    # 创建与CPU核心数相同的进程
    for _ in range(num_cores):
        p = multiprocessing.Process(target=consume_cpu)
        p.start()
        processes.append(p)

    return f"Running {num_cores} processes to consume CPU..."

@app.route('/decrease_cpu')
def decrease_cpu():
    global processes

    # 终止所有占用CPU的进程
    for p in processes:
        p.terminate()
        p.join()

    # 清空进程列表
    processes.clear()

    return "Terminated all CPU-consuming processes. CPU usage should decrease."


@app.route('/cpu_usage')
def cpu_usage():
    # 获取当前CPU使用率
    cpu_percent = psutil.cpu_percent(interval=1)
    return f"Current CPU usage: {cpu_percent}%"

if __name__ == '__main__':
    app.run(debug=True)
