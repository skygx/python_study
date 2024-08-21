#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   get_cols_rows.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/8 下午 1:29   hello      1.0         None

'''
import xlwings as xw
def get_cols_rows(file_path):
    """获取表格总的行数与列数"""
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(file_path)
    sheet = wb.sheets('学生信息表')

    # Excel数据的总行数
    # rows = sheet.api.UsedRange.Rows.count
    # # 列数
    # cols = sheet.api.UsedRange.Columns.count
    # rows = sheet.shape[0]
    # cols = sheet.shape[1]
    rows = sheet.used_range.last_cell.row  # 获取行数
    cols = sheet.used_range.last_cell.column  # 获取列数

    print(f'行数: {rows} \n列数: {cols}')
    wb.close()
    # 退出 Excel 编辑应用
    app.quit()

if __name__ == "__main__":
    file_path = './学生信息表.xlsx'
    # read_xlsx(file_path)
    get_cols_rows(file_path)
