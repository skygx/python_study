# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   ps_net.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/4 下午2:33   hello      1.0         None

'''
import paramiko
import psutil

# 建立SSH连接
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.226.20', username='root', password='root')

# 通过SSH执行命令获取网卡信息
stdin, stdout, stderr = ssh.exec_command('ifconfig')
interface_info = stdout.read().decode()

# 关闭SSH连接
ssh.close()

# 解析网卡信息以获取流量
# 这里需要根据实际的ifconfig输出解析
# 假设输出格式是这样的：RX bytes:xxxx ... TX bytes:yyyy
# interface_name = 'eth0'  # 假设你想要获取的网卡名称是eth0
interface_name = 'ens33'  # 假设你想要获取的网卡名称是eth0

# 解析接收到的字节
rx_bytes = [int(s.split(':')[-1].strip()[:-5]) for s in interface_info.split() if s.startswith(interface_name + 'RX')]
tx_bytes = [int(s.split(':')[-1].strip()[:-5]) for s in interface_info.split() if s.startswith(interface_name + 'TX')]

# 使用psutil获取本地机器网卡流量信息
import psutil

# 获取所有网络接口的名称
network_interfaces = psutil.net_if_addrs()
interface_names = [iface_name for iface_name in network_interfaces.keys() if iface_name != 'lo']

# 初始化流量列表
net_io_stats = []

# 遍历每个网络接口并获取其IO统计信息
for iface_name in interface_names:
    snic = psutil.net_io_counters(pernic=True)[iface_name]
    net_io_stats.append((iface_name, snic.bytes_sent, snic.bytes_recv))

# 打印结果
for name, rx_bytes, tx_bytes in net_io_stats:
    print(f"Interface: {name}")
    print(f"RX: {rx_bytes}")
    print(f"TX: {tx_bytes}")


