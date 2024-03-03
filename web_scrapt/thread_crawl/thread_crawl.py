#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   thread_crawl.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/7 下午 8:32   hello      1.0         None

'''
import text_spider
import threading
import time

def single_thread():
    print("single_thread begin")
    for url in text_spider.urls:
        text_spider.crawl(url)
    print("single_thread end")

def multi_thread():
    print("multi_thread begin")
    threads = []
    for url in text_spider.urls:
        threads.append(
        threading.Thread(target=text_spider.crawl, args=(url,))
        )
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("multi_thread end")

if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread: ", end-start)

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread: ", end - start)
