#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   chat_robot.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/1/10 上午 8:45   hello      1.0         None

'''
import requests
import json
import redis
from functools import lru_cache

# 文心一言配置
api_key = "3MffmglNhft4ooXXBzZSNTHk"
secret_key = "n9Sgu8w9prR1Kc5hyBGx2UD3eGrAVZWR"

# redis配置
redis_host = "192.168.226.20"
redis_port = 6380
redis_passwd = 'admin'
redis_db = 0

class ChatBot:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.message_history = []
        # self.redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_passwd)
        self.chat_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token={}"

    @lru_cache(maxsize =300)
    def get_token(self):
        # if self.redis_client.exists('access_token'):
        #     return self.redis_client.get('access_token').decode()
        # else:
        get_access_token_url = ("https://aip.baidubce.com/oauth/2.0/token?"
                                "client_id={}"
                                "&client_secret={}"
                                "&grant_type=client_credentials").format(
            self.api_key, self.secret_key)
        response = requests.get(get_access_token_url)
        # self.redis_client.setex('access_token', response.json()['expires_in'], response.json()['access_token'])
        return response.json()['access_token']

    def check_tokens(self, total_tokens):
        if total_tokens > 4800:
            self.message_history = self.message_history[len(self.message_history) / 2:]

    def add_chat_history(self, message):
        self.message_history.append(message)
        payload = json.dumps({
            "messages": self.message_history
        })
        return payload

    def send_message(self, message):
        payload = self.add_chat_history({
            "role": "user",
            "content": message
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.chat_url.format(self.get_token()), headers=headers, data=payload)
        self.add_chat_history({
            "role": "assistant",
            "content": response.json()['result']
        })
        return response.json()['result']


if __name__ == '__main__':
    chatbot = ChatBot(api_key, secret_key)
    while True:
        message = input("you: ")
        if message.strip() != "":
            reply = chatbot.send_message(message)
            print("bot: ", reply)
        print(chatbot.get_token.cache_info())
