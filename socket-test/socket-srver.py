#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   socket-srver.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/12  16:23   xguo      1.0         None

'''
import socket

def main():
    s=socket.socket()
    host=socket.gethostname()
    port=1234
    s.bind((host,port))

    s.listen(5)
    while True:
        c,addr=s.accept()
        print("Got connection from",addr)
        c.send(b'Thank you for connecting')
        c.close()

if __name__ == "__main__":
    main()