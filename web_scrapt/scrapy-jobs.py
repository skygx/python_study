#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   scrapy-jobs.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/5  17:07   xguo      1.0         None

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    text = urlopen('http://python.org/jobs').read()
    soup = BeautifulSoup(text, 'html.parser')
    jobs = set()
    for job in soup.body.section('h2'):
        jobs.add('{} ({})'.format(job.a.string, job.a['href']))
    print('\n'.join(sorted(jobs, key=str.lower)))

if __name__ == "__main__":
    main()