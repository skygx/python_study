#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   stanze_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/25 下午 5:11   hello      1.0         None

'''

import stanza

# 下载语言支持
print("Downloading English model...")
stanza.download('en')

# 第一步：构造处理管道，pipeline
en_nlp = stanza.Pipeline('en')

# 第二步：将文本送入管道，管道返回 Document 对象
en_doc = en_nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
print(type(en_doc))

# 第三步：提取分析结果
for i, sent in enumerate(en_doc.sentences):
    print("[Sentence {}]".format(i + 1))
    for word in sent.words:
        print("{:12s}\t{:12s}\t{:6s}\t{:d}\t{:12s}".format( \
            word.text, word.lemma, word.pos, word.head, word.deprel))
    print("")


