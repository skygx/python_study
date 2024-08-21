#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   read_xlsx.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/8 下午 1:27   hello      1.0         None

'''
import xlwings as xw
def read_xlsx(file_path):
    """2、读Excel文档"""
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(file_path)
    # 获取工作表的两种方法
    # sheet = wb.sheets('学生信息表')
    sheet = wb.sheets[0]

    # 获取单个单元格内容
    cell_val = sheet.range(1, 1).value
    cell_A2 = sheet.range('A2').value
    print(cell_val, "\n", cell_A2)
    # 获取多个单元格内容
    row2_col2to4 = sheet.range((2,2), (2,4)).value
    C5_TO_F5 = sheet.range('C5:F5').value
    print(row2_col2to4, '\n', C5_TO_F5)
    # 获取多行数据
    title = sheet.range('A1:F1').value
    data = sheet.range('A2:F5').value
    print(f"title: {title} \n data:")
    for row in data:
        print(row)
    wb.close()
    # 退出 Excel 编辑应用
    app.quit()

if __name__ == "__main__":
    file_path = './学生信息表.xlsx'
    read_xlsx(file_path)
