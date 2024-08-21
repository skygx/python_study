# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   nmap_alive.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/21 下午3:21   hello      1.0         None

'''

# 导入python-nmap库
import nmap
import socket
def nmap_alive(ip, port):
    # 创建nmap对象
    nm = nmap.PortScanner()
    # 设置扫描参数
    nm.scan(ip, port)
    # 获取扫描结果
    state = nm[ip]['tcp'][int(port)]['state']
    if state == 'open':
        print(ip + ':' + port +'is alive')
    else:
        print(ip + ':' + port +'is not alive')

if __name__ == '__main__':
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("本机IP地址为：" + host_ip)
    nmap_alive(host_ip, '3306')
