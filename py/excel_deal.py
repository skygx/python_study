#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:excel_deal.py
    功能:批量处理excel文件
    版本:1.0
    日期:2019/12/1721:14
'''

import pandas as pd
import os

def main():
    file_paths=r'C:\My-goodjob\python\excel'
    files=os.listdir(file_paths)
    for file in files:
        df=pd.read_excel(os.path.join(file_paths,file), sheet_name='total')
        #data=df.loc[0]
        de=df.drop("名字",axis=1)
        data=de.apply(lambda x:x.sum(),axis=1)
        print("获取到所有的值：\n{0}".format(data))

if __name__ == "__main__":
    main()