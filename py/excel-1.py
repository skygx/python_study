#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   excel-1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30  10:44   xguo      1.0         None

'''

import xlsxwriter

def main():
    datas = (
        ['Rent', 1000],
        ['Gas', 100],
        ['Food', 300],
        ['Gym', 50]
    )

    workbook = xlsxwriter.Workbook('ex01.xlsx')
    worksheet = workbook.add_worksheet('data')

    bold = workbook.add_format({'bold': True})
    money = workbook.add_format({'num_format': '$#,##0'})

    worksheet.write('A1', 'Item', bold)
    worksheet.write('B1', 'Cost', bold)

    row, col = 1, 0

    for item, cost in datas:

        worksheet.write(row,col,item)
        worksheet.write(row, col+1, cost)

        row += 1

    worksheet.write(row, 0, 'Total', bold)
    worksheet.write(row, 1, '=SUM(B1:B4)', money)

    workbook.close()


if __name__ == "__main__":
    main()