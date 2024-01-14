#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   send_sms.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/26 下午 5:41   hello      1.0         None

'''

from twilio.rest import Client

# 配置Twilio账户信息
account_sid = "AC4e78d10450b41cc6f0cc5f832423d2c2"
auth_token = "9411343606f8a31c0b0f6f7b8c9079e1"
client = Client(account_sid, auth_token)

# 发送短信
message = client.messages.create(
    to="+8613693367745",
    from_="+17856452462",
    body="测试消息，请勿回复！")
print(f"短信已发送，SID: {message.sid}")
