#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   gradio_inter.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/29 下午 2:51   hello      1.0         None

'''

import random
import gradio as gr
def chat(message, history):
    history = history or []
    message = message.lower()
    if message.startswith("how many"):
        response = random.randint(1, 10)
    elif message.startswith("how"):
        response = random.choice(["Great", "Good", "Okay", "Bad"])
    elif message.startswith("where"):
        response = random.choice(["Here", "There", "Somewhere"])
    else:
        response = "I don't know"
    history.append((message, response))
    return history, history
#设置一个对话窗
chatbot = gr.Chatbot().style(color_map=("green", "pink"))
demo = gr.Interface(
    chat,
    # 添加state组件
    ["text", "state"],
    [chatbot, "state"],
    # 设置没有保存数据的按钮
    allow_flagging="never",
)
demo.launch(server_name='0.0.0.0', server_port=8080, show_error=True)
