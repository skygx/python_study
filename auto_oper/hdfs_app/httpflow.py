#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   httpflow.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/2 上午 9:06   hello      1.0         None

python httpflow.py -r inline access.log > httpflow.txt
'''

from mrjob.job import MRJob
import re

class MRCounter(MRJob):

    def mapper(self, key, line):
        i = 0
        for flow in line.split():
            if i==3:
                timerow=flow.split(":")
                hm=timerow[1] + ":" + timerow[2]
            if i==9 and re.match(r"\d{1,}", flow):
                yield hm, int(flow)
            i += 1

    def reducer(self, key, occurrences):
        yield key, sum(occurrences)

if __name__ == '__main__':
    MRCounter.run()
