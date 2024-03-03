#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   probe_html.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/23 上午 9:27   hello      1.0         None

'''

import os,sys
import time
import sys
import pycurl

# URL="http://www.google.com.hk"
# URL="http://www.baidu.com"
URL="http://192.168.226.20:3000"

def probe_html(URL):
    c=pycurl.Curl()
    c.setopt(pycurl.URL, URL)
    c.setopt(pycurl.CONNECTTIMEOUT, 5)
    c.setopt(pycurl.TIMEOUT, 5)
    c.setopt(pycurl.NOPROGRESS, 1)
    c.setopt(pycurl.FORBID_REUSE, 1)
    c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)

    indexfile=open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")
    c.setopt(pycurl.WRITEHEADER, indexfile)
    c.setopt(pycurl.WRITEDATA, indexfile)

    try:
        c.perform()
    except Exception as e:
        print("connection error: "+str(e))
        indexfile.close()
        c.close()
        sys.exit()

    NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
    CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
    PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
    STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
    TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
    HTTP_CODE = c.getinfo(c.HTTP_CODE)
    SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
    HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
    SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

    print("HTTP状态码: %s"%(HTTP_CODE))
    print("DNS解析时间: %.2f ms"%(NAMELOOKUP_TIME*1000))
    print("建立连接时间: %.2f ms"%(CONNECT_TIME*1000))
    print("准备传输时间: %.2f ms"%(PRETRANSFER_TIME*1000))
    print("传输开始时间: %.2f ms"%(STARTTRANSFER_TIME*1000))
    print("传输结束总时间: %.2f ms"%(TOTAL_TIME*1000))
    print("下载数据包大小: %d bytes/s"%(SIZE_DOWNLOAD))
    print("HTTP头部大小: %d byte"%(HEADER_SIZE))
    print("平均下载速度: %d bytes/s"%(SPEED_DOWNLOAD))

    indexfile.close()
    c.close()

def main():
    probe_html(URL)

if __name__ == '__main__':
    main()
