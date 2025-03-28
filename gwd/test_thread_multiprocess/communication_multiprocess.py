# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   communication_multiprocess.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/26 上午10:27   hello      1.0         None

'''
import multiprocessing
import time

# 进程任务函数
def producer(queue):
    for i in range(5):
        print(f"生产者生产了数据: {i}")
        queue.put(i)  # 将数据放入队列
        time.sleep(1)

def consumer(queue):
    while True:
        data = queue.get()  # 从队列中获取数据
        if data is None:  # 结束标志
            break
        print(f"消费者消费了数据: {data}")

if __name__ == "__main__":
    # 创建队列
    queue = multiprocessing.Queue()

    # 创建进程
    p1 = multiprocessing.Process(target=producer, args=(queue,))
    p2 = multiprocessing.Process(target=consumer, args=(queue,))

    # 启动进程
    p1.start()
    p2.start()

    # 等待生产者完成
    p1.join()

    # 发送结束标志
    queue.put(None)

    # 等待消费者完成
    p2.join()

    print("所有进程执行完毕")
