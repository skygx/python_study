#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   port_scan.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/31  10:59   xguo      1.0         None

'''
import socket
import threading
import nmap

def connScan(host,port):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((host,port))
        print("tcp open port:" + str(port))
    except:
        print('tcp closed:'+str(port))

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP)
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port ' + str(tgtPort))
        connScan(tgtHost, int(tgtPort))

def threadScan(tgtHost, tgtPorts):
    for tgtPort in tgtPorts:
        print('Scanning port ' + str(tgtPort))
        t = threading.Thread(target=connScan, args=(tgtHost,
                                                    int(tgtPort)))
        t.start()

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    results = nmScan.scan(tgtHost, tgtPort)
    state = results['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
    print(" [*] " + tgtHost + " tcp/" + tgtPort + " " + state)
    nmapScan('10.108.x.x','8080')

def main():
    # portScan('www.baidu.com', [80, 443, 3389, 1433, 23, 445])
    # threadScan('www.baidu.com', [80, 443, 3389, 1433, 23, 445])
    nmapScan('www.baidu.com', [80, 443, 3389, 1433, 23, 445])


if __name__ == "__main__":
    main()