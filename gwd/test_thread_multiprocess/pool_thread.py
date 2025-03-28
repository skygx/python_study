# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   pool_thread.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/26 上午10:20   hello      1.0         None

'''
from concurrent.futures import ThreadPoolExecutor
import time

# 线程任务函数
def task(name, delay):
    print(f"线程 {name} 开始运行")
    time.sleep(delay)  # 模拟耗时操作
    print(f"线程 {name} 完成任务, 耗时 {delay} 秒")
    return f"线程 {name} 的结果"

# 创建线程池
with ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务
    future1 = executor.submit(task, "Thread-1", 2)
    future2 = executor.submit(task, "Thread-2", 3)
    future3 = executor.submit(task, "Thread-3", 1)

    # 获取任务结果
    print(future1.result())
    print(future2.result())
    print(future3.result())

print("所有线程执行完毕")
