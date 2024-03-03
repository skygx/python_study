#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   spider.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/7 下午 8:48   hello      1.0         None

'''

import text_spider
import threading
import queue
import time,random

def do_crawl(url_queue:queue.Queue,html_queue:queue.Queue):
    while True:
        url = url_queue.get()
        html = text_spider.crawl(url)
        html_queue.put(html)
        print(threading.current_thread().name, f"crawl{url}", "url_queue_qsize=",url_queue.qsize())
        time.sleep(random.randint(1,2))


def do_parse(html_queue:queue.Queue, fount):
    while True:
        html = html_queue.get()
        results = text_spider.parse(html)
        for result in results:
            fount.write(str(result) + "\n")
        print(threading.current_thread().name, "result size ", "html_queue_qsize=", html_queue.qsize())
        time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()

    for url in text_spider.urls:
        url_queue.put(url)

    for x in range(3):
        t = threading.Thread(target=do_crawl, args=(url_queue, html_queue), name=f"craw{x}")
        t.start()

    fount = open("data.txt","w",encoding="utf-8")
    for x in range(3):
        t = threading.Thread(target=do_parse, args=(html_queue,fount), name=f"parse{x}")
        t.start()
