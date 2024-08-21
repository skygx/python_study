#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   motion_analyse.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/25 下午 5:14   hello      1.0         None

'''

import stanza

# 加载英文预训练模型
nlp = stanza.Pipeline('en')

def analyze_sentiment(text):
    doc = nlp(text)

    sentiment_score = 0
    for sentence in doc.sentences:
        for word in sentence.words:
            if word.sentiment != 0:
                sentiment_score += word.sentiment

    if sentiment_score > 0:
        return "Positive sentiment"
    elif sentiment_score < 0:
        return "Negative sentiment"
    else:
        return "Neutral sentiment"

# 测试情感分析功能
text1 = "This movie is amazing! I love it!"
text2 = "I'm not a fan of this book."

print(analyze_sentiment(text1))  # 输出：Positive sentiment
print(analyze_sentiment(text2))  # 输出：Negative sentiment
