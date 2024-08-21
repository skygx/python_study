#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   entity_out.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/25 下午 5:19   hello      1.0         None

'''
import stanza

# 加载英文预训练模型
nlp = stanza.Pipeline('en')

def extract_entity_relations(text):
    doc = nlp(text)

    for sentence in doc.sentences:
        for ent in sentence.ents:
            if ent.type == 'PERSON':
                person = ent.text
            elif ent.type == 'ORG':
                organization = ent.text

    return f"{person} founded {organization}"

# 测试实体关系抽取功能
text = "Steve Jobs founded Apple Inc. in 1976."

print(extract_entity_relations(text))  # 输出：Steve Jobs founded Apple Inc.
