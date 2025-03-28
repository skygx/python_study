# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   get_netflow.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/4 下午2:35   hello      1.0         None

'''
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

# print(psutil.net_connections('all'))
