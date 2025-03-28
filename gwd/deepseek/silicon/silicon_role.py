# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   data_analyse.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/12 下午5:26   hello      1.0         None

'''
from openai import OpenAI
client = OpenAI(api_key="sk-ujnjhovknhggmlsbhkfwcpjavkzpiubjlkdqsdtxtnvqwvgj", base_url="https://api.siliconflow.cn/v1")

def data_analyse():
    response = client.chat.completions.create(
        model="Qwen/QVQ-72B-Preview",
        messages=[
            {"role": "system", "content": "你是数据分析专家，用Markdown输出结果"},
            # {"role": "user", "content": "分析2024年新能源汽车销售数据趋势"}
            {"role": "user", "content": "分析2024年北京房价数据趋势"}
        ],
        temperature=0.7,
        max_tokens=4096
    )
    return response

def code_generate():
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-Coder-32B-Instruct",
        messages=[{
            "role": "user",
            "content": "编写Python异步爬虫教程，包含代码示例和注意事项"
        }],
        temperature=0.7,
        max_tokens=4096
    )
    return response

def chat_bot():
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[{
            "role": "user",
            "content": "探活url命令，判断返回值是否正常"
        }],
        temperature=0.7,
        max_tokens=4096
    )
    return response

def write_to_file(content):
    with open('../deepsk/data_analyse.md', 'w', encoding='utf-8') as f:
        f.write(content)

# response = data_analyse()
# response = code_generate()
response = chat_bot()

content = response.choices[0].message.content
print(content,end='')

write_to_file(content)
