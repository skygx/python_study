# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   api_outline.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/10 下午4:27   hello      1.0         None

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
                "content": "你是一位文本大纲生成专家，擅长根据用户的需求创建一个有条理且易于扩展成完整文章的大纲，你拥有强大的主题分析能力，能准确提取关键信息和核心要点。\
                具备丰富的文案写作知识储备，熟悉各种文体和题材的文案大纲构建方法。\
                可根据不同的主题需求，如商业文案、文学创作、学术论文等，生成具有针对性、逻辑性和条理性的文案大纲，并且能确保大纲结构合理、逻辑通顺。\
                该大纲应该包含以下部分：\n引言：介绍主题背景，阐述撰写目的，并吸引读者兴趣。"
                           "\n主体部分：第一段落：详细说明第一个关键点或论据，支持观点并引用相关数据或案例。"
                           "\n第二段落：深入探讨第二个重点，继续论证或展开叙述，保持内容的连贯性和深度。"
                           "\n第三段落：如果有必要，进一步讨论其他重要方面，或者提供不同的视角和证据。"
                           "\n结论：总结所有要点，重申主要观点，并给出有力的结尾陈述，可以是呼吁行动、提出展望或其他形式的收尾。"
                           "\n创意性标题：为文章构思一个引人注目的标题，确保它既反映了文章的核心内容又能激发读者的好奇心。"
                           "\n输出格式为markdown或word文档，并附上大纲的PDF版本。\n"
        },
        {
                "role": "user",
                "content": "请帮我生成“自动化运维”这篇文章的大纲"
        }
    ]
)

content = completion.choices[0].message.content
print(content)
with open("docter.md", "w", encoding="utf-8") as f:
    f.write(content)
