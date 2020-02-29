#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   analyse-job1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/21  10:38   xguo      1.0         None

'''
import pandas as pd
import pandas_profiling

def main():
    df=pd.read_csv('lagou-devops.csv')
    pandas_profiling.ProfileReport(df)

if __name__ == "__main__":
    main()