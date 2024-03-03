#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   ip_get_info.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/22 下午 3:38   hello      1.0         None

'''

from IPy import IP

def main():
    ip_s = input('Please input an IP or net-range: ')
    ips = IP(ip_s)

    if len(ips) > 1:
        print('net: %s' % ips.net())
        print('netmask: %s' % ips.netmask())
        print('broadcast: %s' % ips.broadcast())
        print('reverse address: %s' % ips.reverseNames()[0])
        print('subnet: %s' % len(ips))
    else:
        print('reverse address: %s' % ips.reverseNames()[0])

    print('hexadecimal: %s' % ips.strHex())
    print('binary: %s' % ips.strBin())
    print('iptype: %s' % ips.iptype())


if __name__ == '__main__':
    main()
