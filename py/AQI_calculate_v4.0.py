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
'''

import json
import csv
import os

def process_json_file(file):
    with open(file,mode='r',encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)
    return city_list

def process_csv_file(file):
    with open(file,mode='r',encoding='utf-8',newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row) )
    # return city_list

def main():
    pathfile = input("请输入文件名称：")
    filename,file_ext = os.path.splitext(pathfile)

    if file_ext == '.json':
        process_json_file(pathfile)
    elif file_ext == '.csv':
        process_csv_file(pathfile)
    else:
        print('不支持数据格式')

if __name__ == "__main__":
    main()