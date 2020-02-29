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
2019/3/9 11:10   xguo      6.0         通过bs4获取网页指定信息
2019/3/11 11:23  xguo      7.0         用pandas读取csv文件，并提取信息
'''

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():

   csv = pd.read_csv('city_aqi.csv')
   print(csv[['City','AQI']].sort_values('AQI').head(4))
   print(csv.info())

   print(csv.head())

   print('AQI最大值：',csv['AQI'].max())
   print('AQI最小值：',csv['AQI'].min())
   print('AQI均值：',csv['AQI'].mean())

   top5_cities = csv.sort_values(by=['AQI']).head(5)
   print('空气质量最好的5个城市：')
   print(top5_cities)

   top5_bottom_cities = csv.sort_values(by=['AQI'],ascending=False).head(5)
   print('空气质量最差的5个城市：')
   print(top5_bottom_cities)

   print(csv[csv['AQI']>40])

   top5_cities.plot(kind='bar',x='City',y='AQI',title='空气质量最好的5个城市',figsize=(10,10))
   plt.savefig('top5_aqi.png')
   plt.show()

if __name__ == "__main__":
    main()