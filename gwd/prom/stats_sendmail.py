#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   stats_sendmail.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/5 上午 10:36   hello      1.0         None

'''
import psutil
import smtplib
from email.mime.text import MIMEText

cpu_percent = psutil.cpu_percent()
print(cpu_percent)

if cpu_percent > 10:
    try:
        server = smtplib.SMTP('smtp.126.com')
        server.login('sweet_love2000@126.com', 'QYNOJLCRJQERNQUF')

        message = 'CPU 使用率超过 80%：当前使用率为 {}%'.format(cpu_percent)
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = 'sweet_love2000@126.com'
        msg['To'] = 'sweet_love2000@126.com'
        # subject = '警报：高 CPU 使用率'.encode('utf-8')
        msg['Subject'] = '警报：高 CPU 使用率'

        server.sendmail(msg['From'], msg['To'], msg.as_string())
        print("邮件已成功发送")
    except Exception as e:
        print("发送邮件时出现错误:", str(e))
    finally:
    # 关闭与SMTP服务器的连接
        server.quit()
