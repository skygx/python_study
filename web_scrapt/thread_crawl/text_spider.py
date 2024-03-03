#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   queue_scrapt.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/7 下午 8:16   hello      1.0         None

'''
'''
课题：实现生产者消费者模式的多线程爬虫
https://quotes.toscrape.com/page/1/
课堂知识点
l、多组件pipeline:技术架构
2、生产者消费者爬虫架构
3、多线程数据通信的queue.Queue
4、代码编写来实现生产者消费者爬虫

涉及到的模块
requests请求与响应
bs4解析模块
threading多线程
queue队列

队列
Queue.qsize0返回队列的大小
Queue.empty（）如果队列为空，返回True,反之False
Queue..full如果队列满了，返回True,反之False
Queue.get()获取队列
Queue.get_nowait()相当于Queue.get(False),非阻塞方法
Queue.put(item)写入队列
Queue.task_done{}在完成一项工作之后，Queue.task_done（）函数向任务已经完成的队列发送一个信号。
Queue.joinO实际上意味者等到队列为空，冉执行别的操作

什么是爬虫
批量抓取网页信息的自动化工具
通用爬虫 -- 浏览器-一范围广
聚焦爬虫 -- 针对性

爬虫的工作原理
模拟浏览器，向服务器发送一个http请求，当服务器接收到请求之后，会向爬虫返回数据
'''
import requests
from bs4 import BeautifulSoup

urls = [f"https://fabiaoqing.com/biaoqing/lists/page/{page}.html"
        for page in range(1,51)]

# print(urls)

def crawl(url):
    resp = requests.get(url)
    return resp.text

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find("div", class_="ui segment imghover")
    return [(link['href'],link["title"]) for link in links.find_all("a")]

if __name__ == '__main__':
    for result in parse(crawl(urls[0])):
        print(result)

