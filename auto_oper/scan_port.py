#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   scan_port.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/12 上午 9:40   hello      1.0         None

'''

import socket
import argparse
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('host')
args = parser.parse_args()
start = time.time()

try:
    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((args.host, port))
        if result == 0:
            print("Port: {} Open".format(port))
        sock.close()
except KeyboardInterrupt:
    sys.exit()

end = time.time()
print(f"Scanning completed in: {end-start:.3f}s")
