#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   event_trigger.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/4/3 下午 1:53   hello      1.0         None

'''

import threading
import time

# 创建一个事件对象
event = threading.Event()


def wait_for_event():
    # 线程等待事件的通知
    event.wait()  # 如果event.is_set()是False，则等待直到它变为True
    print("Event trigger!")


def trigger_event():
    # 线程触发事件
    print("Event is being set...")
    time.sleep(2)  # 等待2秒
    event.set()  # 设置事件，解除等待状态
    print("Event has been set.")


# 创建并启动等待事件的线程
waiter = threading.Thread(target=wait_for_event)
waiter.start()

# 创建并启动触发事件的线程
trigger = threading.Thread(target=trigger_event)
trigger.start()
