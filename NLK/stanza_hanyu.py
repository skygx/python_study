#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   stanza_hanyu.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/28 上午 10:41   hello      1.0         None

'''

import stanza

# 下载语言支持
print("Downloading Chinese model...")
stanza.download('zh', verbose=False)

# 第一步：构造处理管道，pipeline
zh_nlp = stanza.Pipeline('zh', processors='tokenize,lemma,pos,depparse', verbose=False, use_gpu=False)

# 第二步：将文本送入管道，管道返回 Document 对象
zh_doc = zh_nlp("达沃斯世界经济论坛是每年全球政商界领袖聚在一起的年度盛事。")
print(type(zh_doc))

# 第三步：提取分析结果
for i, sent in enumerate(zh_doc.sentences):
    print("[Sentence {}]".format(i + 1))
    for word in sent.words:
        print("{:12s}\t{:12s}\t{:6s}\t{:d}\t{:12s}".format( \
            word.text, word.lemma, word.pos, word.head, word.deprel))
    print("")
