#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   word_count_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/28 16:14   xguo      1.0         None

'''
from collections import Counter
import re

def main():
    #读取文件
    f = open(r'E:\project\python\python_study\python_study\wordcount_test.txt','r')
    words = []
    #切分保存到数组
    lines = f.readlines()
    for line in lines:
        line = line[:-1]
        line = re.sub(r'\s+',' ',line)
        # print(line)

        word = line.split(' ')
        words.extend(word)
    # print(words)
    #Counter统计数组中数量
    c = Counter(words)
    print(c)

    f.close()

if __name__ == "__main__":
    main()