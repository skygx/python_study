# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   share_multiprocess.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/26 上午10:40   hello      1.0         None

'''
import multiprocessing

# 进程任务函数
def increment(shared_value, lock):
    for _ in range(100000):
        with lock:  # 加锁
            shared_value.value += 1

if __name__ == "__main__":
    # 共享内存
    shared_value = multiprocessing.Value("i", 0)  # 初始值为 0
    lock = multiprocessing.Lock()  # 线程锁

    # 创建多个进程
    processes = []
    for _ in range(4):
        process = multiprocessing.Process(target=increment, args=(shared_value, lock))
        processes.append(process)

    # 启动进程
    for process in processes:
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()

    print(f"最终 shared_value 的值: {shared_value.value}")
