# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   silicon_api.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/12 下午4:27   hello      1.0         None

'''
from openai import OpenAI

client = OpenAI(api_key="sk-ujnjhovknhggmlsbhkfwcpjavkzpiubjlkdqsdtxtnvqwvgj", base_url="https://api.siliconflow.cn/v1")
response = client.chat.completions.create(
    model='deepseek-ai/DeepSeek-V2.5',
    messages=[
        {'role': 'user',
        # 'content': "中国大模型行业2025年将会迎来哪些机遇和挑战"
        'content': "自动化运维"
         }
    ],
    stream=True
)

# print(response)
for chunk in response:
    print(chunk.choices[0].delta.content, end='')
