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
'''

import json
import csv

def process_json_file(file):
    f = open(file,mode='r',encoding='utf-8')
    city_list = json.load(f)
    return city_list

def main():
    pathfile = input("请输入文件名称：")
    city_list = process_json_file(pathfile)
    city_list.sort(key=lambda city:city['aqi'])

    lines = []
    lines.append(city_list[0].keys())
    for city in city_list:
        lines.append(city.values())

    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()

if __name__ == "__main__":
    main()