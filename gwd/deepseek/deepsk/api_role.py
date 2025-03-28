# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   api_role.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/10 下午5:08   hello      1.0         None

'''
from openai import OpenAI

client = OpenAI(
    base_url="https://api.deepseek.com/",
    api_key="sk-4e5e5cf7e18b48198f08289f20ba70d4"
)

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
                "role": "user",
                # "content": "假设你想和领导请5天年假，现在工作比较多，领导可能不想让你请，请模拟两个人展开一段对话。"
                "content": "患者：2025.3.10 \
             郭某，男，40岁，近半个月，每天晚上10点入睡，夜里3点左右会醒再难入睡，眼睛会疼痛"
        }
    ]
)

print(completion.choices[0].message.content)
