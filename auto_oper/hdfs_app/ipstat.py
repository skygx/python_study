#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   ipstat.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/2 上午 9:24   hello      1.0         None

ipstat.py -r inline access.log > ipstat.txt
'''
from mrjob.job import MRJob
import re
IP_RE = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

class MRCounter(MRJob):

    def mapper(self, key, line):
        for ip in IP_RE.findall(line):
            yield ip, 1

    def reducer(self, ip, occurrences):
        yield ip, sum(occurrences)

if __name__ == '__main__':
    MRCounter.run()
