# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   basic_multiprocess.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/26 上午10:26   hello      1.0         None

'''
import multiprocessing
import time

# 定义一个进程任务函数
def task(name, delay):
    print(f"进程 {name} 开始运行")
    time.sleep(delay)  # 模拟耗时操作
    print(f"进程 {name} 完成任务, 耗时 {delay} 秒")

if __name__ == "__main__":
    # 创建多个进程
    process1 = multiprocessing.Process(target=task, args=("Process-1", 2))
    process2 = multiprocessing.Process(target=task, args=("Process-2", 3))

    # 启动进程
    process1.start()
    process2.start()

    # 等待所有进程完成
    process1.join()
    process2.join()

    print("所有进程执行完毕")
