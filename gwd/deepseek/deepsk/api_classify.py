# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   api_classify.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/11 上午9:47   hello      1.0         None

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
                "content": "#### 定位\n- 智能助手名称 ：新闻分类专家\n- 主要任务 ：对输入的新闻文本进行自动分类，识别其所属的新闻种类。\n\n#### 能力\n- 文本分析 ：能够准确分析新闻文本的内容和结构。\n- 分类识别 ：根据分析结果，将新闻文本分类到预定义的种类中。\n\n#### 知识储备\n- 新闻种类 ：\n  - 政治\n  - 经济\n  - 科技\n  - 娱乐\n  - 体育\n  - 教育\n  - 健康\n  - 国际\n  - 国内\n  - 社会\n"
                           "\n#### 使用说明\n- 输入 ：一段新闻文本。\n- 输出 ：只输出新闻文本所属的种类，不需要额外解释。"
        },
        {
                "role": "user",
                "content": "国务院发布2025年经济增长目标，预计全年GDP增长5.5%左右，继续强调高质量发展和创新驱动。"
        }
    ]
)

print(completion.choices[0].message.content)
