# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   test_1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/1/29 下午4:03   hello      1.0         None

'''
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='deepseek-r1:8b', messages=[
  {
    'role': 'user',
    'content': '为什么天空是蓝色的?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
# print(response.message.content)

# stream = chat(
#     model='llama3.2:1b',
#     messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
#     stream=True,
# )
#
# for chunk in stream:
#   print(chunk['message']['content'], end='', flush=True)

