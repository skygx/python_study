#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   ku6_video.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/2 下午 8:19   hello      1.0         None

'''

import requests
import json

url = "https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"}
response = requests.get(url,headers=headers).text
# print(type(response))

req = json.loads(response)
# print(type(req))

datas = req['data']
# print(datas)

video = {}
for data in datas:
    data_title = data['title']
    data_url = data['playUrl']
    # video[title] = url

    #获取网页二进制视频数据
    video_data = requests.get(url=data_url,headers=headers).content

    #目的： 下载视频  sys open urllib--urlretrieve
    #视频数据属于二进制数据，必须转换数据类型 content. 写入要是二进制wb

    with open('.\\video\\' + data_title, mode='wb') as f:
        f.write(video_data)
        print(f'下载成功： {data_title}')

#爬虫： https协议 数据解析方式 多线程多进程 scrapy框架 分布式爬虫 反爬虫技术 js逆向
#数据分析： pandas numpy 数据可视化
