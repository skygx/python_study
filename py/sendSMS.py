#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   sendSMS.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/20  11:06   xguo      1.0         None

'''
import os
from twilio.rest import Client

def main():
    # Your Account SID from twilio.com/console
    account_sid = "AC4e78d10450b41cc6f0cc5f832423d2c2"
    # Your Auth Token from twilio.com/console
    auth_token = "f5081238d2709a6750459f91585c92cb"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+8613693367745",
        from_="+16173000436",
        body="Hello from Python Twilio!")

    print(message.sid)


if __name__ == "__main__":
    main()