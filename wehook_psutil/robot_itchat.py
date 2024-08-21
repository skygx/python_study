#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   robot_itchat.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/8 上午 11:49   hello      1.0         None

'''

#import itchat
#itchat.auto_login() #登陆 二维码
#itchat.send("hello, lover",toUserName='semen99')
#to_name1 = itchat.search_friends(name='丰盛富足的迈迈')
#print(to_name1)
#itchat.send('你好~', toUserName=to_name1[0]['UserName']) #发送文字

#from wxpy import *
#bot = Bot(cache_path=True)
#bot.file_helper.send("hello")
#BASE_URL = "https://login.weixin.qq.com"
#USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"

import time
import requests
import json

class WeChat:
    def __init__(self):
        self.CORPID = 'ww1f22d25661b0d6a4'  #企业ID，在管理后台获取
        self.CORPSECRET = 'AsC2v2-XRbfzseyau0eqvoLSpiTuMwIVB6CCuTa4cuI'#自建应用的Secret，每个自建应用里都有单独的secret
        self.AGENTID = '1000002'  #应用ID，在后台应用中获取
        self.TOUSER = "guoxin"  # 接收者用户名,多个用户用|分割

    def _get_access_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        values = {'corpid': self.CORPID,
                  'corpsecret': self.CORPSECRET,
                  }
        req = requests.post(url, params=values)
        data = json.loads(req.text)
        # print(data["access_token"])
        return data["access_token"]

    def send_data(self, message):
        send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self._get_access_token()
        print(send_url)
        send_values = {
            "touser": self.TOUSER,
            "msgtype": "text",
            "agentid": self.AGENTID,
            "text": {
                "content": message
                },
            "safe": "0"
            }
        send_msges=(bytes(json.dumps(send_values), 'utf-8'))
        respone = requests.post(send_url, send_msges)
        respone = respone.json()   #当返回的数据是json串的时候直接用.json即可将respone转换成字典
        return respone["errmsg"]


if __name__ == '__main__':
    wx = WeChat()
    wx.send_data("这是程序发送的第1条消息！\n Python程序调用企业微信API,从自建应用“告警测试应用”发送给管理员的消息！")
    wx.send_data("这是程序发送的第2条消息！")
