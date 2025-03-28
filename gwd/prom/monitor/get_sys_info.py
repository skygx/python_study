# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   get_sys_info.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/4 下午3:07   hello      1.0         None

'''
import json
import psutil
import datetime
import socket
import uuid

# 获取Mac地址
def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

# 磁盘 磁盘的使用量等等
def get_my_computer():
    # 获取主机名
    hostname = socket.gethostname()
    # 获取IP
    ip = socket.gethostbyname(hostname)
    # 系统用户
    users_list = ",".join([u.name for u in psutil.users()])
    # print(u"当前有%s个用户，分别是%s" % (users_count, users_list))
    # 系统启动时间
    start_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    sys_info = {"hostname": hostname, "ip": ip, "mac": get_mac_address(), "user": users_list, "start_time": start_time}

    # 01.cpu信息
    cpu1 = psutil.cpu_count()
    cpu2 = str(psutil.cpu_percent(interval=1)) + '%'
    # print(u"物理CPU个数 %s" % psutil.cpu_count(logical=False))
    cpu = {"amount": cpu1, "rate": cpu2}

    # 02.内存信息
    mem = psutil.virtual_memory()
    mem_total = round(mem.total / 1024 / 1024 / 1024, 2)
    mem_free = round(mem.free / 1024 / 1024 / 1024, 2)
    mem_percent = str(mem.percent) + '%'
    mem_used = round(mem.used / 1024 / 1024 / 1024, 2)
    ddr = {"total": mem_total, "free": mem_free, "rate": mem_percent, "used": mem_used}

    # 03.磁盘信息(磁盘空间使用占比)
    io = psutil.disk_partitions()
    disk = []
    for i in io:
        # print(i.device)
        o = psutil.disk_usage(i.device)
        disk_data = {"disk_name": i.device,
                     "total": round(o.total / (1024.0 * 1024.0 * 1024.0),1),
                     "used": round(o.used / (1024.0 * 1024.0 * 1024.0),1),
                     "surplus": round(o.free / (1024.0 * 1024.0 * 1024.0),1),
                     "rate": psutil.disk_usage(i.device).percent}
        disk.append(disk_data)

    # 04.网卡，可以得到网卡属性，连接数，当前流量等信息
    net_info = psutil.net_io_counters()
    bytes_sent = '{0:.2f}'.format(net_info.bytes_recv / 1024 / 1024) # mb
    bytes_rcvd = '{0:.2f}'.format(net_info.bytes_sent / 1024 / 1024)
    net = {"bytes_sent": bytes_sent, "bytes_rcvd": bytes_rcvd}

    # 数据字典
    data = {"sys": sys_info, "cpu": cpu, "ddr": ddr, "disk": disk, "net": net}
    return data

if   __name__ == '__main__':
    data = get_my_computer()
    re = json.dumps(data)
    print(data)
