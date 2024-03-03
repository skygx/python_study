#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   send_sms.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/10 下午 9:23   hello      1.0         None

'''
import requests
import json

def send_notice(event_name,key,text):
    url = f"https://maker.ifttt.com/trigger/{event_name}/with/key/{key}"
    payload = {"value1": text}
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    print(response.text)

if __name__ == '__main__':
    text = "又是全新的一天！"
    send_notice("hello","bPvIj7TQYtFekKVlmrF7eoFQGc9neuRIGkw4Mm7LcG7", text)
