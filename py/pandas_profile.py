#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   pandas_profile.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/3  16:03   xguo      1.0         None

'''
import pandas as pd
import pandas_profiling
import cufflinks as cf
import plotly as py

def main():
    df=pd.read_excel("../data/picc-machine-20200619.xlsx",sheet_name="朝阳门虚拟机")
    # profile=pandas_profiling.ProfileReport(df)
    # profile.to_file(output_file="../dist/machine.html")
    cf.go_offline()
    cf.set_config_file(offline=False,world_readable=True)
    plt=py.offline.plot
    plt(df,filename='../disk/base.html')
    # df.iplot()


if __name__ == "__main__":
    main()