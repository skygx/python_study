# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   psutil_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/4 下午2:20   hello      1.0         None

'''
# !/usr/bin/python3
import psutil
import datetime
import time
import socket
from elasticsearch import Elasticsearch
import sched
import logging
import configparser

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 日志配置
# logging.basicConfig(level=logging.config.get('log_config')['log_level'],
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='monitor.log',
#                     filemode='w')

# 创建日志对象
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建文件处理程序
file_handler = logging.FileHandler('log_file.log')
file_handler.setLevel(logging.INFO)

# 创建格式化器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 添加文件处理程序到logger
logger.addHandler(file_handler)

# 使用自定义连接类初始化Elasticsearch对象
# host = "192.168.226.20"
# port = 9200
# username = "elastic"
# password = "elastic"
host = config['es_config']['es_host']
port = config['es_config']['es_port']
username = config['es_config']['es_username']
password = config['es_config']['es_password']

try:
    es = Elasticsearch([{'host': host, 'port': port}], http_auth=(username, password))
    # es = Elasticsearch("http://elastic:elastic@192.168.226.20:9200")
    # print("连接成功")
    logger.info("连接成功")
except Exception as e:
    logger.error("连接失败", e)
def linux_monitor():
    sys_info={}
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    # cpu的使用率
    cpu_per = psutil.cpu_percent()
    # 内存使用率
    mem_per = psutil.virtual_memory().percent
    # 磁盘使用率
    disk_per = psutil.disk_usage('/').percent
    # 网络使用情况  收发多少数据 net.bytes_recv、net.bytes_sent
    net = psutil.net_io_counters()
    # net = psutil.net_io_counters(pernic=True)['ens33']
    # 获取当前系统时间
    current_time = datetime.datetime.now()
    # 拼接显示
    str = "监控信息:\n"
    str += "|--------ip---------|--hostname--|---------time--------|---cpu---|----memory----|----disk----|--------------net-------------|\n"
    str += "| %s |   %s  |    %s     |   %s%%  |    %s%%     |    %s%%   | recv:%.2fMB  sent:%.2fMB |\n" \
           % (ip, hostname, current_time.strftime("%F %T"), cpu_per, mem_per, disk_per, net.bytes_recv / 1024 / 1024, net.bytes_sent / 1024 / 1024)
    logger.info(str)
    # print("IP:", ip)
    # print("Hostname:", hostname)
    sys_info['hostname'] = hostname
    sys_info['ip'] = ip
    sys_info['cpu_per'] = cpu_per
    sys_info['mem_per'] = mem_per
    sys_info['disk_per'] = disk_per
    sys_info['net_recv'] = round(net.bytes_recv / 1024 / 1024,2)
    sys_info['net_sent'] = round(net.bytes_sent / 1024 / 1024,2)
    sys_info['current_time'] = current_time.isoformat() + "+0800"
    # 写入es
    return sys_info

def task():
    sys_info = linux_monitor()
    index_name = config['es_config']['es_index']
    es.index(index=index_name, body=sys_info)
    logger.info("写入成功")

def loop_monitor():
    scheduler = sched.scheduler(time.time, time.sleep)
    while True:
        scheduler.enter(10, 1, task, ())
        scheduler.run()

if __name__ == '__main__':
    loop_monitor()

    # query = {'query': {'match_all': {}}}
    # res = es.search(index=index_name, body=query)
    # print(res)
