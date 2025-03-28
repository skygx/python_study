# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   deal_data.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/12/4 下午1:35   hello      1.0         None

'''

import pandas as pd
import math
import os
import re
# from pandas import read_excel,DataFrame
# from math import fabs
# from os import path,getcwd,mkdir,listdir
# from re import match


def deal_data(file_path):

    sheet_name = "外包人员考勤记录"
    data = pd.read_excel(file_path, sheet_name=sheet_name)

    time = data['考勤时长（小时）'].dropna()
    # print(time)
    deal_time = time.apply(lambda x: float(str(x-1).split('.')[0] + '.' + str(x-1).split('.')[1][:1]) if 1 <= x <= 15  else 14)
    # print(deal_time)
    origin_time = round(time.sum(),2)
    sum_time = round(deal_time.sum(),1)
    dates = len(deal_time)
    diff_time = round(math.fabs(origin_time - sum_time),2)
    # print(sum_time)
    return origin_time,sum_time,dates,diff_time

def main():
    names = []
    origin_times = []
    sum_times = []
    dates = []
    diff_times = []
    name_time = {}

    if os.path.exists(os.path.join(os.getcwd(),'统计')):
        pass
    else:
        os.mkdir(os.path.join(os.getcwd(),'统计'))

    for file in os.listdir():
        if re.match(r"^.*\.xlsx$", file):
            name = os.path.splitext(file)[0]
            # print(name)
            names.append(name)
            origin,time,date,diff = deal_data(file)
            origin_times.append(origin)
            sum_times.append(time)
            dates.append(date)
            diff_times.append(diff)
            print(name,origin, time, date, diff)
    data = pd.DataFrame({'姓名':names,'原始工时':origin_times,'总工时':sum_times,'工时天数':dates,'工时误差':diff_times})
    data.to_excel(os.path.join(os.getcwd(),'统计','工时统计.xlsx'),index=False)
    # pd.DataFrame(name_time,index=[0]).to_excel(os.path.join(os.getcwd(),'统计','工时统计.xlsx'))

if __name__ == '__main__':
    main()
