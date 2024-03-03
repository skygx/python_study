#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   robot_wehook.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/8 上午 11:06   hello      1.0         None

'''

import hmac
import hashlib
import base64
import urllib.parse
from time import time
from datetime import datetime,timedelta
import requests
import psutil as psu
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import robot_itchat
import robot_email


'''
钉钉机器人数字签名计算
'''
def get_digest():
    # 取毫秒级别时间戳，round(x, n) 取x小数点后n位的结果，默认取整
    timestamp = str(round(time() * 1000))
    secret = 'SECa1919437b1b27597d866b9a372a6c6a15bc8485d0ebf5125e48bc19595560b21'
    secret_enc = secret.encode('utf-8')  # utf-8编码
    string_to_sign = '{}\n{}'.format(timestamp, secret)  # 字符串格式化拼接
    string_to_sign_enc = string_to_sign.encode('utf-8')  # utf-8编码
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()  # HmacSHA256算法计算签名
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))  # Base64编码后进行urlEncode
    #  返回时间戳和计算好的编码拼接字符串，后面直接拼接到Webhook即可
    return f"&timestamp={timestamp}&sign={sign}"

def warning_bot(msg):

    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "【简说Python】今日福利",
            "text": msg
        },
        "at": {
          "atMobiles": [
              "13693367745"  # 要@对象的手机号
          ],
        }
    }
    # 机器人链接地址，发post请求 向钉钉机器人传递指令
    webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=1ceb7263e9491e3fb7ec80b3b2337035400d928c513e6f38ac502e239bb1a750'
    # 利用requests发送post请求
    req = requests.post(webhook_url+get_digest(), json=data)


'''
云服务器基础数据
服务器已运行时间、负载状态、CPU使用率、运行内存使用率、物理内存使用率
'''


def get_server_info():
    # 获取系统的基本数据
    # 服务器已运行时间=现在时间和服务器开启时间之差
    run_times = str(timedelta(seconds=int(time()) - int(psu.boot_time())))
    # 系统负载状态（最近1、5、15分钟）
    loadavg = [round(i, 2) for i in psu.getloadavg()]
    # CPU使用率 测试间隔0.3秒
    cpu_in_use = psu.cpu_percent(interval=0.3)
    # 系统运行内存使用率
    # 内存使用率大于80% 触发报警
    vm_in_use = psu.virtual_memory().percent
    vm_available = round(psu.virtual_memory().available / (1024 ** 3), 2)
    # 系统物理存储使用率
    disk_in_use = psu.disk_usage('/').percent
    disk_free = round(psu.disk_usage('/').free / (1024 ** 3), 2)

    # 还可以添加进程、线程等信息，后面专门安排一篇文章写

    base_info = f"""您的云服务器已运行: {run_times}，
- 机器负载情况为(最近1、5、15分钟)：{loadavg}，
- 目前CPU使用率为：{cpu_in_use}%，
- 系统运行内存使用率为：{vm_in_use}%，
- 剩余可用运行内存为：{vm_available}GiB，
- 系统存储内存使用率为：{disk_in_use}%，
- 剩余可用存储内存为：{disk_free}GiB

**{'机器CPU使用率正常' if cpu_in_use <= 80 else '机器CPU使用率过高，可能触发预警'}**
"""
    return base_info, loadavg, cpu_in_use, vm_in_use, disk_in_use

'''
服务器预警设置
本篇先简单点，只设置负载和CPU使用率预警
'''
def get_warning():
    base_info, loadavg, cpu_in_use, vm_in_use, disk_in_use = get_server_info()
    # 首先判断服务器负载情况
    # 只看近一分钟和近十五分钟情况 应该<= 0.7*CPU数量
    loadavg_max = psu.cpu_count() * 0.7
    loadavg_max = 0.01  # 测试使用，正式环境请注释掉
    if loadavg[0] >= loadavg_max and loadavg[2] >= loadavg_max:
        warning1 = f'⚠️<font color="#d30c0c">【警告】</font>您的云服务器当前负载率为(最近1、5、15分钟)-{loadavg}，负载率已达<font color="#d30c0c">{round(loadavg[2] / loadavg_max, 2) * 100}%</font>，请及时检查系统是否存在问题，也可以@我，发送：基础信息，查看云服务器基础信息。'
        return warning1

    if cpu_in_use >= 80:
        warning2 = f'⚠️<font color="#d30c0c">【警告】</font>您的云服务器当前CPU使用率为<font color="#d30c0c">{cpu_in_use}%</font>，请及时检查系统是否存在问题，也可以@我，发送：基础信息，查看云服务器基础信息。'
        return warning2
    return 'ok'

'''
1、每天早上9:00 发送服务器情况到钉群
'''

def every_day_nine():
    message = get_server_info()[0]
    title = '服务器基础信息'
    warning_bot(message, title)

'''
2、时时预警（每30秒检测一次）
'''

def every_seconds_30():
    warning = get_warning()
    if warning != 'ok':
        title = '【⚠️警告】服务器故障'
        warning_bot(warning, title)

'''
3、@机器人，自动问答设置
下一篇安排，需要另外新建一个企业机器人
和群聊机器人流程不一样～
'''

# 选择BlockingScheduler调度器
sched = BlockingScheduler(timezone='Asia/Shanghai')

# job_every_nine 每天早上9点运行一次  日常发送
sched.add_job(every_day_nine, 'cron', hour=21, minute=55)

# every_seconds_30 每30s执行一次  数据监控
sched.add_job(every_seconds_30, 'interval', seconds=3)

# 启动定时任务
#sched.start()

if __name__ == '__main__':
    base_info, loadavg, cpu_in_use, vm_in_use, disk_in_use = get_server_info()
    warning_bot(base_info)
    wx = robot_itchat.WeChat()
    wx.send_data(base_info)
    em = robot_email.Email()
    em.send_data(base_info)
