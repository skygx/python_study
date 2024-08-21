#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   textblob_test1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/4/1 下午 3:52   hello      1.0         None

'''
from textblob import TextBlob

text = "Hello, this is a sample sentence. How are you?"
blob = TextBlob(text)

# 分词为单词
words = blob.words
print(words)

# 分词为句子
sentences = blob.sentences
print(sentences)

text = "Python is a great programming language."
blob = TextBlob(text)

# 进行词性标注
tags = blob.tags
print(tags)

text = "Python is a great programming language."
blob = TextBlob(text)

# 提取名词短语
noun_phrases = blob.noun_phrases
print(noun_phrases)

text = "I love Python programming."
blob = TextBlob(text)

# 进行情感分析
sentiment = blob.sentiment
print(sentiment)

text = "我喜欢Python编程。"
blob = TextBlob(text)

# 进行情感分析
sentiment = blob.sentiment
print(sentiment)

text = "Hello，how are you？"
blob = TextBlob(text)

# 将文本翻译为法语
# translated_blob = blob.translate(to='fr')
# print(translated_blob)

feedback = "这个产品非常棒，强烈推荐！"
blob = TextBlob(feedback)

# 对反馈进行情感分析
sentiment = blob.sentiment
print(sentiment)

message = "你好，你好吗？"
blob = TextBlob(message)

# 将消息翻译为西班牙语
# translated_blob = blob.translate(to='es')
# print(translated_blob)
