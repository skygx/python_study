#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   weather_get.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/16 下午 8:24   hello      1.0         None

'''
import requests
from pyquery import PyQuery as pq
import xlwt

def main():
    # 获取网页源代码
    html = requests.get('https://tianqi.so.com/weather/').text

    # 解析网页
    html = pq(html)
    datas = html.find('ul.weather-columns li div').items()

    # 去除空白信息
    datas = [r.text() for r in datas if r.text() != '']

    # 将表头和内容合并
    table = ['日期', '天气', '温度', '空气', '风速及风向'] + datas

    # 新建工作簿
    wb = xlwt.Workbook(encoding='utf-8')

    # 新建工作表
    ws = wb.add_sheet('北京 15日天气', cell_overwrite_ok=True)

    # 填入内容
    for i, r in enumerate(table):
        ws.write(i // 5, i % 5, r)

    # 保存工作表
    wb.save('北京 15日天气.xls')

if __name__ == '__main__':
    main()
