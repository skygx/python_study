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

def deal_data(file_path):

    sheet_name = "工时"
    data = pd.read_excel(file_path, sheet_name=sheet_name)

    time = data['工时'].dropna()
    # print(time)
    deal_time = time.apply(lambda x: float(str(x-1).split('.')[0] + '.' + str(x-1).split('.')[1][:1]) if 1 <= x <= 15  else 14)
    # print(deal_time)
    sum_time = round(deal_time.sum(),1)
    dates = len(deal_time)
    # print(sum_time)
    return sum_time,dates

def main():
    names = []
    sum_times = []
    dates = []
    name_time = {}
    for file in os.listdir():
        if re.match(r"^.*\.xlsx$", file):
            name = os.path.splitext(file)[0]
            # print(name)
            names.append(name)
            time,date = deal_data(file)
            sum_times.append(time)
            dates.append(date)
            print(name, time, date)
    data = pd.DataFrame({'姓名':names,'总工时':sum_times,'工时天数':dates})
    data.to_excel(os.path.join(os.getcwd(),'统计','工时统计.xlsx'),index=False)
    # pd.DataFrame(name_time,index=[0]).to_excel(os.path.join(os.getcwd(),'统计','工时统计.xlsx'))

if __name__ == '__main__':
    main()
