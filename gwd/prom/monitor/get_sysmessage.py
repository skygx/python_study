# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   get_sysmessage.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/11/18 下午4:27   hello      1.0         None

'''
import psutil
import socket
import paramiko
# 远程计算机的IP地址


def get_sys_info(hostname,username,password,cmd,port=22):
    # 尝试连接到远程计算机
    try:
        # 创建一个SSHClient对象
        # from ssh import SSHClient

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接服务器
        ssh.connect(hostname=hostname, port=port, username=username, password=password)

        # 获取系统信息
        system_info = ssh.exec_command(cmd)[1].read().decode('utf-8')
        # cpu_percent = ssh.exec_command('psutil.cpu_percent()')[1].read().decode('utf-8')
        # mem_info = ssh.exec_command('psutil.virtual_memory().percent')[1].read().decode('utf-8')
        print(system_info)

        # 获取CPU信息
        # cpu_percent = client.run_command('psutil_linux.cpu_percent(interval=1)')
        # print(cpu_percent)

        # 获取内存信息
        # mem_info = client.run_command('psutil.virtual_memory()')
        # print(mem_info)

    except socket.error as e:
        print(f"无法连接到 {hostname}: {e}")
def main():
    hostname = '192.168.226.20'
    get_sys_info(hostname, 'root', 'root',cmd='uname -a')

if __name__ == '__main__':
    main()
