#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   dns_simple.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/21 下午 1:32   hello      1.0         None

'''

import dns.resolver
import os
import http.client

iplist = []
appdomain="www.baidu.com"

def get_iplist(domain=""):
    try:
        A = dns.resolver.resolve(domain, 'A')
    except Exception as e:
        print("dns resolver error:"+str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                iplist.append(j.address)
    return True

def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
    http.client.socket.setdefaulttimeout(5)
    conn = http.client.HTTPConnection(checkurl)

    try:
        conn.request("GET", "/", headers={"Host": appdomain})
        r = conn.getresponse()
        getcontent = r.read(15)
        print(getcontent)
    finally:
        if b"html" in getcontent:
            print(ip+" [OK]")
        else:
            print(ip+" [Error]")


if __name__ == '__main__':
    if get_iplist(appdomain) and len(iplist)>0:
        for ip in iplist:
            checkip(ip)
    else:
        print("dns resolver error")
