# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   ps_msg.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/19 下午2:24   hello      1.0         None

'''
import psutil

# # 获取所有正在运行的进程PID
# pid_list = psutil.pids()
# print(pid_list)

# 获取指定PID的进程
p = psutil.Process(8)
print(p)
print("进程名:", p.name())
print("进程的可执行绝对路径: ", p.exe())
print("进程当前的工作目录: ", p.cwd())
print("调用此进程的命令行: ", p.cmdline())
print("进程PID: ", p.pid)
print("进程的父PID: ", p.ppid())
print("进程的子进程: ", p.children())
print("进程的父进程(对象): ", p.parent())
print("进程的父进程(列表): ", p.parents())
print("进程的状态: ", p.status())
print("拥有该进程的用户: ", p.username())
print("进程创建的时间: ", p.create_time())
print("进程累计的时间: ", p.cpu_times())
print("进程的CPU占用率: ", p.cpu_percent())
print("进程的CPU亲和性: ", p.cpu_affinity())
print("进程的内存信息: ", p.memory_info())
print("进程的内存占用率: ", p.memory_percent())
print("进程映射的内存区域: ", p.memory_maps())
print("进程的I/O信息: ", p.io_counters())
print("进程打开的文件信息: ", p.open_files())
print("进程打开的套接字连接: ", p.connections())
print("进程使用的线程数: ", p.num_threads())
print("进程打开的线程: ", p.threads())
print("进程执行的上下文切换数量: ", p.num_ctx_switches())
print("进程的优先级(带参数则可设置优先级): ", p.nice())
print("进程的I/O优先级(带参数则可设置优先级): ", p.ionice())
print("进程的环境变量: ", p.environ())
print("进程信息（字典）: ", p.as_dict())
print("进程是否正在运行: ", p.is_running())
