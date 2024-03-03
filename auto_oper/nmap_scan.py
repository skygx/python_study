#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   nmap_scan.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/25 上午 9:04   hello      1.0         None

192.168.226.10/32 1-1000
192.168.226.0/24 80,443,22

'''

import sys
import nmap

scan_row=[]
input_data = input('Please input hosts and port: ')
scan_row = input_data.split(' ')
if len(scan_row) != 2 :
    print("Input errors,example '192.168.1.0/24 80,443,22'")
    sys.exit(0)
hosts=scan_row[0]
port=scan_row[1]

try:
    nm = nmap.PortScanner()
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

try:
    nm.scan(hosts=hosts, arguments=' -v -sS -p '+port)
except Exception as e:
    print("Scan error:"+str(e))

for host in nm.all_hosts():
    print('-------------------------------------------------------------------------')
    print('Host : %s (%s) ' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('-----------------------------')
        print('Protocol : %s' % proto)

        lport = sorted(nm[host][proto].keys())

        # lport.sort()
        for port in lport:
            print('port : %s\tstate : %s' % (port,nm[host][proto][port]['state']))
