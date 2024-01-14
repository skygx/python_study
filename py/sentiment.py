#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   sentiment.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/12/12 下午 5:23   hello      1.0         None

'''


from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print(sentiment)
    if sentiment > 0.3:
        return "积极"
    elif sentiment < 0.2:
        return "消极"
    else:
        return "中性"


if __name__ == "__main__":
    text = input("请输入要分析的文本：")
    sentiment = analyze_sentiment(text)
    print(f"文本情感倾向：{sentiment}")
