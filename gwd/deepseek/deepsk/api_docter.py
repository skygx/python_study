# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   api_docter.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/11 上午8:54   hello      1.0         None

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
                "role": "system",
                "content": "你是一位专家级医生，可以根据你的专业知识为客户提供高质量的医疗服务。\
                具备丰富的医学知识、医学术语、医学专业词汇等，能够准确、清晰地解读客户的需求，并提供专业的医疗建议。\
                可根据不同的病患需求，如心脏病、呼吸系统疾病、肾脏病、失眠、精神疾病等，提供不同的治疗方案。\
                该治疗方案应该包含以下部分：\n病症、诊断、治疗方案、饮食建议、用药指导(建议药品)、注意事项等。"                           
                           "\n输出格式为markdown或word文档，并附上大纲的PDF版本。\n"
        },
        {
                "role": "user",
                "content": "患者，40岁，男性，患者感到头痛、发热，并有轻微咳嗽。希望能得到专业的医疗建议。"
        }
    ]
)

def write_to_file(content):
    with open("docter.md", "w", encoding="utf-8") as f:
        f.write(content)

content = completion.choices[0].message.content
print(content)


#write_to_file(content)
