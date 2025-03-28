# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   get_ip.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/4 下午2:55   hello      1.0         None

'''
import socket
import psutil

# 获取主机名
hostname = socket.gethostname()
print(f"Hostname: {hostname}")
ip = socket.gethostbyname(hostname)
print(f"IP Address: {ip}")


# 获取主机的IP地址
def get_host_ip():
    try:
        # 对于IPv4
        ipv4_info = [nic_info for nic_info in psutil.net_if_addrs() if nic_info[0] != 'lo0'][0][1][0]
        return ipv4_info
    except IndexError:
        return "No IPv4 address found"
    except Exception as e:
        return str(e)


# ip_address = get_host_ip()
# print(f"IP Address: {ip_address}")
