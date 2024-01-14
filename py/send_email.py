#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   send_email.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/13 上午 10:57   hello      1.0         None

'''

from email.mime.text import MIMEText
from email.header import Header
import smtplib
import sys

#发送邮件服务器
# smtpserver = 'smtp.126.com'
smtpserver = 'smtp.qq.com'

#邮箱账号/密码
# user = 'sweet_love2000@126.com'
# password = 'ACTQLFXCJZRJNDZX'
user="38286261@qq.com"
password = 'sfhuaxqnonalbjgg'

#发件箱
sender = '38286261@qq.com'

#收件箱
receiver = 'guoxin_well@126.com'

#主题
subject = 'Python email test1'

#正文
msg = MIMEText('<html><h1>Hello Python!</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = sender
msg['To'] = receiver

try:
    # smtp = smtplib.SMTP()
    smtp = smtplib.SMTP_SSL(smtpserver)
    smtp.connect(smtpserver,465)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
except:
    print(sys.exc_info())
