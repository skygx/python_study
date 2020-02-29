#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   AQI_calculate_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/5 10:24   xguo      1.0         AQI计算
2019/3/5 10:24   xguo      2.0         读取json文件
2019/3/7 15:00   xguo      3.0         输出到csv格式文件
2019/3/7 15:30   xguo      4.0         添加判断文件是csv还是json
2019/3/8 9:00    xguo      5.0         实现爬虫抓取pm25.in实时数据
'''

from bs4 import BeautifulSoup
import requests

def get_html_text(url):
    r = requests.get(url,timeout=30)
    print(r.status_code)
    return r.text

def main():
    city_pinyin = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)

    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">    
    '''

    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_val = url_text[begin_index:end_index]
    print("空气质量为：{}".format(aqi_val))

if __name__ == "__main__":
    main()