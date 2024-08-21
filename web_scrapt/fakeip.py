#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   fakeip.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/19 上午 8:53   hello      1.0         None

'''
from scapy.all import *
from faker import Faker
import random
import ipaddress
import socket
import struct

ip=socket.inet_ntoa(struct.pack('>I', random.randrange(1, 0xffffffff)))
print(ip)

IPV4 = ipaddress.IPv4Address._ALL_ONES
def random_ipv4():
    return ipaddress.IPv4Address._string_from_ip_int(
        random.randint(0, IPV4)
    )
print(random_ipv4())

fake = Faker()
ip_addr = fake.ipv4()
print(ip_addr)

ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
print(ip)

def send_fake_ip_packet(source_ip, destination_ip):
    # 构造一个IP数据包，设置源IP地址和目的IP地址
    # packet = IP(src=source_ip, dst=destination_ip)
    #
    # # 发送数据包
    # send(packet)
    # 构造IP数据包
    packet = IP(src=source_ip, dst=destination_ip) / TCP(
        dport=80) / "GET / HTTP/1.1\nHost: 192.168.226.20\n\n"

    # 发送数据包
    response = sr1(packet)

    # 打印响应
    print(response.summary())

# 设置源IP地址和目的IP地址
source_ip = ip_addr
destination_ip = "192.168.226.20"

# 发送伪造IP地址的数据包
send_fake_ip_packet(source_ip, destination_ip)
