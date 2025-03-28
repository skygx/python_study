# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   sync_thread.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/26 上午10:16   hello      1.0         None

'''
import threading

# 共享资源
counter = 0
lock = threading.Lock()

# 线程任务函数
def increment():
    global counter
    for _ in range(100000):  # 对共享资源进行 100000 次加 1
        lock.acquire()  # 加锁
        counter += 1
        lock.release()  # 解锁

# 创建多个线程
threads = []
for i in range(10):
    thread = threading.Thread(target=increment)
    threads.append(thread)

# 启动线程
for thread in threads:
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print(f"最终 counter 的值: {counter}")
