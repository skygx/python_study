#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   splite_character.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/11/21 下午 4:57   hello      1.0         None

'''

def add_line_break(text, n):
    lines = [text[i:i+n] for i in range(0, len(text), n)]
    return "\n".join(lines)

def add_line_break2(text, n):
    result = ""
    for i in range(0, len(text), n):
        result += text[i:i+n] + "\n"
    return result.strip()

with open("D:/project/Pyproject/python_study/txt/xingshi.txt","r",encoding="utf-8") as f:
    words=f.read()

# formatted_text="\n".join(words)
formatted_text=add_line_break2(words,4)
print(formatted_text)

# with open("D:/project/Pyproject/python_study/txt/words.txt","w",encoding="utf-8") as f:
#     words=f.write(formatted_text)
