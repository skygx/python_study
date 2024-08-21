# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   socket_alive.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/21 下午3:16   hello      1.0         None

'''

import socket

def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((host, port))
        sock.close()
        return True
    except:
        return False
    finally:
        sock.close()

if __name__ == '__main__':
    ip = "192.168.226.20"
    ports = [80, 8080, 8081, 8082, 9090, 5601, 8091]
    for port in ports:
        if check_port(ip, port):
            print(f"{ip}:{port} is alive")
        else:
            print(f"{ip}:{port} is not alive")

