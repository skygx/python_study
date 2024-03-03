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
from tkinter import *
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

    @lru_cache(maxsize=300)
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

def show():
    m1=message.get()
    r1=chatbot.send_message(m1)
    print(f'you: {m1}')
    print(f'robot: {r1}')
    e2.delete(1.0, END)  # 清空文本区域内容
    e2.insert(INSERT, r1)


if __name__ == '__main__':
    chatbot = ChatBot(api_key, secret_key)
    root = Tk()

    message = StringVar()
    reply = StringVar()
    frame = Frame(root)
    frame.pack()
    root.title("chatrobot")

    # 创建一个Text控件并设置其属性

    e1 = Entry(frame, textvariable=message, width=100)
    e2 = Text(frame, width=100, height=20, wrap=WORD,font = ('楷体',12))
    scrollbar = Scrollbar(frame, orient="vertical", command=e2.yview)
    e2['yscrollcommand'] = scrollbar.set
    # e2.insert('end', reply)
    Label(frame, text="you:",font = ('楷体',16)).grid(row=0, column=0)
    Label(frame, text="robot:",font = ('楷体',16)).grid(row=1, column=0)

    # 将Text控件放置到Frame上
    e1.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    e2.grid(row=1, column=1, sticky='nsew')
    scrollbar.grid(row=1, column=2, sticky='ns')

    Button(frame, text="回答", command=show).grid(row = 2,column = 1,sticky = N)

    root.mainloop()
