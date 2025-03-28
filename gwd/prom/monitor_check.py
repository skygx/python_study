# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   monitor_check.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/27 下午2:35   hello      1.0         None

'''
import psutil
import time

def collect_system_metrics():
    # CPU 使用率
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=True)

    # 内存使用情况
    mem = psutil.virtual_memory()
    mem_total = round(mem.total / (1024 ** 3), 2)  # GB
    mem_used = round(mem.used / (1024 ** 3), 2)
    mem_percent = mem.percent

    # 磁盘 I/O
    disk_io = psutil.disk_io_counters()
    disk_read = disk_io.read_bytes / (1024 ** 2)  # MB
    disk_write = disk_io.write_bytes / (1024 ** 2)

    # 网络流量
    net_io = psutil.net_io_counters()
    net_sent = net_io.bytes_sent / (1024 ** 2)  # MB
    net_recv = net_io.bytes_recv / (1024 ** 2)

    # 磁盘使用率
    disk_usage = psutil.disk_usage("/")
    disk_total = round(disk_usage.total / (1024 ** 3), 2)  # GB
    disk_used = round(disk_usage.used / (1024 ** 3), 2)
    disk_percent = disk_usage.percent

    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "cpu": {"percent": cpu_percent, "cores": cpu_count},
        "memory": {"total": mem_total, "used": mem_used, "percent": mem_percent},
        "disk": {
            "total": disk_total,
            "used": disk_used,
            "percent": disk_percent,
            "read": disk_read,
            "write": disk_write,
        },
        "network": {"sent": net_sent, "recv": net_recv},
    }

if __name__ == "__main__":
    metrics = collect_system_metrics()
    print(metrics)
