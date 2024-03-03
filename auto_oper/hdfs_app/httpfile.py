#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   httpfile.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/2 上午 9:26   hello      1.0         None

python httpfile.py -r inline access.log > httpfile.txt
'''
from mrjob.job import MRJob
import re

class MRCounter(MRJob):

    def mapper(self, key, line):
        i = 0
        for url in line.split():
            if i==6:
                yield url, 1
            i += 1

    def reducer(self, url, occurrences):
        yield url, sum(occurrences)

if __name__ == '__main__':
    MRCounter.run()
