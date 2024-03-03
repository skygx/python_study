#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   robot_email.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/8 下午 2:07   hello      1.0         None

'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
#设置服务器所需信息
#163邮箱服务器地址
class Email:
    def __init__(self):
        self.HOST = 'smtp.126.com'
        self.USER = 'sweet_love2000@126.com'
        self.PASSWORD = 'QVICEYSYCTYPXZQO'
        self.SENDER = "sweet_love2000@126.com"  # 发送者用户名
        self.RESERVERS = "sweet_love2000@126.com"

    def send_data(self,msg):
        # 设置email信息
        # 邮件内容设置
        message = MIMEText(msg, 'plain', 'utf-8')
        # 邮件主题
        message['Subject'] = Header('服务器信息', 'utf-8')
        # 发送方信息
        message['From'] = self.SENDER
        # 接受方信息
        message['To'] = self.RESERVERS
        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(self.HOST, 25)
            # 登录到服务器
            smtpObj.login(self.USER, self.PASSWORD)
            # 发送
            smtpObj.sendmail(
                self.SENDER, self.RESERVERS, message.as_string())
            # 退出
            smtpObj.quit()
            print('success')
        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误

if __name__ == '__main__':
    em = Email()
    em.send_data('hello')
