#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   send_smtp_mail.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/23 上午 8:35   hello      1.0         None

'''
import smtplib
import string

# HOST="smtp.126.com"
# TO="guoxin_well@126.com"
# FROM="guoxin_well@exam.com"
HOST="192.168.226.20"
TO="bar@exam.com"
FROM="guoxin@exam.com"
SUBJECT="Test email from Python"
text="Python rules them all!"
BODY=f'''From: {FROM}
To: {TO}
Subject: {SUBJECT}

{text}'''

print(BODY)
try:
    server = smtplib.SMTP()
    server.connect(HOST,"1025")
    # server.login("sweet_love2000@126.com","EVOYKIKWNSZAELNX")
    server.login("foo@exma.com","guoxin")
    server.sendmail(FROM,[TO],BODY)
    server.quit()
    print("邮件发送成功")
except Exception as e:
    print("失败： "+str(e))
