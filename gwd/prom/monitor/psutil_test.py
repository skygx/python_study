# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   psutil_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/4 下午2:20   hello      1.0         None

'''
# !/usr/bin/python3
import psutil
import datetime
import elasticsearch


def linux_monitor():
    # cpu的使用率
    cup_per = psutil.cpu_percent()
    # 内存使用率
    mem_per = psutil.virtual_memory().percent
    # 磁盘使用率
    disk_per = psutil.disk_usage('/').percent
    # 网络使用情况  收发多少数据 net.bytes_recv、net.bytes_sent
    net = psutil.net_io_counters()
    # 获取当前系统时间
    current_time = datetime.datetime.now().strftime("%F %T")
    # 拼接显示
    str = ""
    str += "|---------time--------|---cpu---|----memory----|----disk----|--------------net-------------|\n"
    str += "| %s |   %s%%  |    %s%%     |    %s%%   | recv:%.2fMB  sent:%.2fMB |\n" \
           % (current_time, cup_per, mem_per, disk_per, net.bytes_recv / 1024 / 1024, net.bytes_sent / 1024 / 1024)
    print(str)


linux_monitor()

