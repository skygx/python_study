#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   multi_thread_map.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/26  15:24   xguo      1.0         None

'''

import urllib.request
from multiprocessing.dummy import Pool as ThreadPool


def main():


    urls = [
        'http://www.baidu.com',
        'http://www.sina.com',
        'http://www.126.com',
        'http://www.163.com',
        'http://www.taobao.com',
        'http://www.jd.com',
        'http://www.tmall.com',
        'https://www.pinduoduo.com',
        'http://www.sohu.com',
        'http://www.china.com.cn',
        # etc..
    ]

    # Make the Pool of workers
    pool = ThreadPool(4)
    # Open the urls in their own threads
    # and return the results
    results = pool.map(urllib.request.urlopen, urls)
    for result in results:
        # print(type(result))
        print(result.info())
    # close the pool and wait for the work to finish
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()