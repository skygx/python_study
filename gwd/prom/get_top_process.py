# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   get_top_process.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/27 下午4:31   hello      1.0         None

'''
import psutil

def get_top_cpu_processes(n=3):
    # 获取所有进程信息
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            # 收集每个进程的PID、名称和CPU使用率
            processes.append({
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'cpu': proc.info['cpu_percent']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass  # 忽略无法访问的进程

    # 按CPU使用率降序排序
    sorted_processes = sorted(processes, key=lambda p: p['cpu'], reverse=True)

    # 只返回前N个进程
    return sorted_processes[:n]


if __name__ == "__main__":
    # 获取CPU总使用率
    cpu_percent = psutil.cpu_percent(interval=1)  # 采样1秒

    print(f"当前CPU总使用率: {cpu_percent}%\n")
    print("CPU使用率最高的前3个程序:")

    top_processes = get_top_cpu_processes(3)
    for i, proc in enumerate(top_processes, 1):
        print(f"{i}. {proc['name']} (PID: {proc['pid']}): {proc['cpu']:.2f}%")
