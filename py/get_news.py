#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   get_news.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/9 上午 9:43   hello      1.0         None

'''
import newspaper
from newspaper import Config, Article, Source

config = Config()
config.memoize_articles = False
config.http_success_only=True
config.fetch_images=False
config.browser_user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
config.request_timeout=2



def get_info(article):
    try:
        article.download()
        article.parse()
        title=article.title
        if "车" in title or "广告"  in title:
            return "广告"
        print(title)
        # print(article.authors)
        # print(article.summary)
        # print(article.text)
        # print(article.keywords)
        # print(article.nlp())
    except:
        print("html error")

def get_url(url):
    paper = newspaper.build(url, config=config)
    articles = paper.articles

    for article in articles[:]:
        # print(article)
        get_info(article)


if __name__ == '__main__':
    url = 'http://www.sina.com.cn/'
    paper = newspaper.build(url, config=config)
    for category in paper.category_urls():
        print(category)
        get_url(category)
    # http://health.sina.com.cn
    # http://eladies.sina.com.cn
    # http://english.sina.com
    # ...

    # url="https://edition.cnn.com/"
    # url = 'http://www.sina.com.cn/'
    # url='https://news.baidu.com/'
    # url='https://www.chinanews.com.cn/dwq/2023/01-08/9930119.shtml'

    # sina_paper = newspaper.build(url, language='zh')

