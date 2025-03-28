# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   text_use.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/30 上午10:33   hello      1.0         None

'''

if __name__ == '__main__':
    text = "This is a test. This is only a test."
    word_count = len(text.split())
    print(f"Word count: {word_count}")

    text = "Hello, World!"
    new_text = text.replace("World", "Python")
    print(new_text)

    text = "apple,banana,orange"
    fruits = text.split(',')
    print(fruits)

    fruits = ['apple', 'banana', 'orange']
    text = ', '.join(fruits)
    print(text)

    text = "Hello, World!"
    if "World" in text:
        print("Found 'World' in the text.")

    text = "    Hello,   World!   "
    no_space_text = text.replace(" ", "")
    print(no_space_text)
