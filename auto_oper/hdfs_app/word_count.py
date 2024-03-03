#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   word_count.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/1 上午 9:03   hello      1.0         None

python word_count.py -r inline input.txt > output.txt
'''

from mrjob.job import MRJob

class MRWordCounter(MRJob):
    def mapper(self, key, value):
        for word in value.split():
            yield word, 1
    def reducer(self, word, occurrences):
        yield word, sum(occurrences)

if __name__ == '__main__':
    MRWordCounter.run()
