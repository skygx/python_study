# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   popl_multiprocess.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/26 上午10:39   hello      1.0         None

'''
import multiprocessing
import time

# 进程任务函数
def task(name, delay):
    print(f"进程 {name} 开始运行")
    time.sleep(delay)  # 模拟耗时操作
    print(f"进程 {name} 完成任务, 耗时 {delay} 秒")
    return f"进程 {name} 的结果"

if __name__ == "__main__":
    # 创建进程池
    with multiprocessing.Pool(processes=3) as pool:
        # 提交任务
        result1 = pool.apply_async(task, args=("Process-1", 2))
        result2 = pool.apply_async(task, args=("Process-2", 3))
        result3 = pool.apply_async(task, args=("Process-3", 1))

        # 获取任务结果
        print(result1.get())
        print(result2.get())
        print(result3.get())

    print("所有进程执行完毕")
