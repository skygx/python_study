#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   http_minute_conn.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/2 上午 9:21   hello      1.0         None

python http_minute_conn.py -r inline access.log > http_minute_conn.txt

远程hadoop执行
python http_minute_conn.py -r hadoop --jobconf mapreduce.job.priority=VERY_HIGH --jobconf mapred.map.tasks=2 --jobconf mapred.reduce.tasks=1 -o hdfs://192.168.226.20:9000/output/minute_conn hdfs://192.168.226.20:9000/nginx
'''

from mrjob.job import MRJob
import re

class MRCounter(MRJob):

    def mapper(self, key, line):
        i = 0
        for dt in line.split():
            if i==3:
                timerow=dt.split(":")
                hm=timerow[1] + ":" + timerow[2]
                yield hm, 1
            i += 1

    def reducer(self, key, occurrences):
        yield key, sum(occurrences)

if __name__ == '__main__':
    MRCounter.run()
