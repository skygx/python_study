#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   httpstatus.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/2 上午 9:14   hello      1.0         None

python httpstatus.py -r inline access.log > httpstatus.txt
'''

from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class MRCounter(MRJob):

    def mapper(self, key, line):
        i = 0
        for httpcode in line.split():
            if i==8 and re.match(r"\d{1,3}", httpcode):
                yield httpcode, 1
            i += 1

    def reducer(self, httpcode, occurrences):
        yield httpcode, sum(occurrences)

    def steps(self):
        return [MRStep(mapper=self.mapper),
                MRStep(reducer=self.reducer)]

if __name__ == '__main__':
    MRCounter.run()
