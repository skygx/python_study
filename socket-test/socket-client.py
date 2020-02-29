#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   socket-client.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/12  16:25   xguo      1.0         None

'''
import socket

def main():
    s=socket.socket()
    host=socket.gethostname()
    port=1234

    s.connect((host,port))
    print(s.recv(1024))

if __name__ == "__main__":
    main()