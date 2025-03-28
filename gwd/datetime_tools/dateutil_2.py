# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   dateutil_2.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/18 上午10:56   hello      1.0         None

'''
from  dateutil.parser  import  parse
from  dateutil.tz  import  gettz

def  parse_fuzzy_date(date_string):
        try:
                return  parse(date_string,  fuzzy=True)
        except  ValueError:
                return  None

dates  =  [
        "明天下午3点",
        "3天后的早上9点",
        "下周二晚上8点",
        "2023年6月1日"
]

for  date  in  dates:
        parsed  =  parse_fuzzy_date(date)
        if  parsed:
                print(f"'{date}'  解析为:  {parsed}")
        else:
                print(f"无法解析  '{date}'")
