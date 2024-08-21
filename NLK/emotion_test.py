#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   emotion_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/26 下午 1:50   hello      1.0         None

'''
import paddlehub

senta = paddlehub.Module(name='senta_lstm')
input_word=""
while input_word != 'q':
    input_word=input("请输入需要情绪检测的句子：\n")
    result = senta.sentiment_classify(data={'text': [input_word]})
    print("情绪状态：",result[0]['sentiment_key'])
    print("情绪得分是：",100*result[0]['positive_probs'])
