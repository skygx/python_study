#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   excel_deal-v1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/31  10:20   xguo      1.0         取picc-machine数据，指定列输出

'''

import pandas as pd
import os

class Excel_Deal:
    def __init__(self,file,sheet):
        self.file=file
        self.sheet=sheet

    def get_df(self):
        sheet = self.sheet
        file = self.file
        df=pd.read_excel(file,sheet_name=sheet)
        return df

    def deal_excel(self):

        test_data=[]

        df=self.get_df()

        #获得excel文件中总行数和总列数
        print(f'rows: {df.shape[0]}   columns: {df.shape[1]}')

        #获得文件所有列名
        head=df.columns.values

        #修改列名
        df.columns=['vir_use','vir_ip','hostname','ip','cpu_num','mem','disk','os','usage']

        #指定输出列名
        # trans_head=[head[0],head[2],head[3],head[-1]]

        trans_head=['vir_use','hostname','cpu_num','mem','usage']

        for i in df.index.values:
            row_data=df.loc[i,trans_head]

            test_data.append(row_data)
         # 选择指定行   cpu_num > 4
        # data = df.loc[df['cpu_num'] > 4, trans_head]

        data = df.loc[(df['cpu_num'] > 4) & (df['mem'].replace('G','') > '2'),trans_head].sort_values(by=['mem'],ascending=False,kind='quicksort')
        print(data)

        #制作输出数据格式
        test = pd.DataFrame(columns=trans_head, data=test_data)

        #保存数据到csv文件
        test.to_csv('../data/test.csv',index=False,sep=',')
        # print(test)

    def get_sheets(self):
        file = self.file
        df = pd.ExcelFile(file)
        sheet=df.sheet_names
        print(sheet)
        print(f'sheets number: {len(sheet)}')
        return sheet

def main():
    deal=Excel_Deal(r'../data/picc-machine-20200619.xlsx','朝阳门虚拟机')
    deal.deal_excel()
    # deal.get_sheets()

if __name__ == "__main__":
    main()