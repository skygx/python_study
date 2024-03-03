#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   ip_msg.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/22 下午 3:25   hello      1.0         None

'''
from IPy import IP

def main():
    print('net info')
    print(IP('10.0.0.0/8').version())
    print(IP('::1').version())
    ip = IP('192.168.0.0/24')
    print(ip.len())
    for x in ip:
        print(x)
    ip = IP('192.168.1.20')
    print(ip.reverseName())
    print(ip.iptype())

    print('net data convert')
    ip = IP('8.8.8.8')
    print(ip.iptype())
    print(ip.int())
    print(ip.strHex())
    print(ip.strBin())

    print('net mask')
    print(IP('192.168.1.0').make_net('255.255.255.0'))
    print(IP('192.168.1.0/255.255.255.0',make_net=True))
    print(IP('192.168.1.0-192.168.1.255',make_net=True))

    print('net segment')
    print(IP('192.168.1.0/24').strNormal(0))
    print(IP('192.168.1.0/24').strNormal(1))
    print(IP('192.168.1.0/24').strNormal(2))
    print(IP('192.168.1.0/24').strNormal(3))

    print('net calculator')
    print(IP('10.0.0.0/24') < IP('12.0.0.0/24'))
    print(IP('192.168.1.100') in IP('192.168.1.0/24'))
    print(IP('192.168.1.0/24') in IP('192.168.0.0/16'))
    print(IP('192.168.0.0/23').overlaps('192.168.1.0/24'))
    print(IP('192.168.1.0/24').overlaps('192.168.2.0'))

if __name__ == '__main__':
    main()
