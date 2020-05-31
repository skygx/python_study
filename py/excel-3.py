#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   excel-3.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30  13:17   xguo      1.0         None

'''

from datetime import datetime
import xlsxwriter


def main():
    # 数据准备
    datas = (
        ['Rent', '2018-05-13', 1000],
        ['Gas', '2018-05-14', 100],
        ['Food', '2018-05-16', 300],
        ['Gym', '2018-05-20', 50],
    )

    # 创建表格
    workbook = xlsxwriter.Workbook('ex03.xlsx')
    worksheet = workbook.add_worksheet('data')

    # 添加格式
    bold_f = workbook.add_format({'bold': True})
    money_f = workbook.add_format({'num_format': '$#,##0'})
    # 添加日期格式new
    date_f = workbook.add_format({'num_format': 'mmmm d yyyy'})

    # 添加对齐方式和表格宽度new
    worksheet.set_column(1, 1, 15)

    # 添加表头数据
    worksheet.write('A1', 'Item', bold_f)
    worksheet.write('B1', 'Date', bold_f)
    worksheet.write('C1', 'Cost', bold_f)

    # 定义偏移值
    row, col = 1, 0
    # 添加数据
    for item, date, cost in datas:
        date = datetime.strptime(date, '%Y-%m-%d')
        worksheet.write(row, col, item)
        worksheet.write_datetime(row, col + 1, date, date_f)
        worksheet.write(row, col + 2, cost, money_f)
        row += 1

    # 添加计数
    worksheet.write(row, 0, 'Total', bold_f)
    worksheet.write(row, 2, '=SUM(C2:C5)', money_f)

    # 存储并关闭
    workbook.close()


if __name__ == "__main__":
    main()