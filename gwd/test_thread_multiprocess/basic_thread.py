# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   basic_thread.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/26 上午10:15   hello      1.0         None

'''
import threading
import time

# 定义一个线程任务函数
def task(name, delay):
    print(f"线程 {name} 开始运行")
    time.sleep(delay)  # 模拟耗时操作
    print(f"线程 {name} 完成任务, 耗时 {delay} 秒")

# 创建多个线程
thread1 = threading.Thread(target=task, args=("Thread-1", 2))
thread2 = threading.Thread(target=task, args=("Thread-2", 3))

# 启动线程
thread1.start()
thread2.start()

# 等待所有线程完成
thread1.join()
thread2.join()

print("所有线程执行完毕")
