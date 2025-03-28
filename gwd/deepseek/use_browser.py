# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   use_browser.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/16 上午8:05   hello      1.0         None

'''
import asyncio
from browser_use import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()


async def main():
    # 创建一个使用 DeepSeek 模型的浏览器代理
    agent = Agent(
        task="在百度首页上查看百度热搜，并提取出前10条热搜新闻标题",
        llm=ChatOpenAI(
            base_url='https://api.deepseek.com/v1',
            model='deepseek-reasoner',
            api_key=os.getenv('DEEPSEEK_API_KEY'),
        ),
        use_vision=False,  # 启用视觉能力
    )

    # 执行任务
    result = await agent.run()
    print(f"任务结果: {result}")


if __name__ == "__main__":
    asyncio.run(main())
