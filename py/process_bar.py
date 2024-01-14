#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   process_bar.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/8 下午 8:29   hello      1.0         None

'''
import time
import sys
from tqdm import tqdm
from alive_progress import alive_bar
import PySimpleGUI  as sg
import progressbar

def process_bar1():
    for i in range(1, 101):
        print("\r", end="")
        print("进度: {}%: ".format(i), "▓" * (i // 2), end="")
        sys.stdout.flush()
        time.sleep(0.05)

def process_bar2():
    t = 60
    print("**************带时间的进度条**************")
    start = time.perf_counter()
    for i in range(t + 1):
        finsh = "▓" * i
        need_do = "-" * (t - i)
        progress = (i / t) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finsh, need_do, dur), end="")
        time.sleep(0.05)

def process_bar3():
    for i in tqdm(range(1, 60)):
        """
        代码
        """
        # 假设这代码部分需要0.05s，循环执行60次
        time.sleep(0.05)

def process_bar4():
    with alive_bar(len(range(100))) as bar:
        for item in range(100):  # 遍历任务
            bar()  # 显示进度
            """
            代码
            """
            # 假设这代码部分需要0.05s
            time.sleep(0.05)

def process_bar5():
    count = range(100)
    for i, item in enumerate(count):
        sg.one_line_progress_meter('实时进度条', i + 1, len(count), '-key-')
        """
        代码
        """
        # 假设这代码部分需要0.05s
        time.sleep(0.05)

def process_bar6():
    p = progressbar.ProgressBar()
    # # 假设需要执行100个任务，放到ProgressBar()中
    for i in p(range(100)):
        """
        代码
        """
        # 假设这代码部分需要0.05s
        time.sleep(0.05)

if __name__ == '__main__':
    process_bar1()
    process_bar2()
    process_bar3()
    process_bar4()
    process_bar5()
    process_bar6()
