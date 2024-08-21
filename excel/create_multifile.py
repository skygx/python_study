#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   create_multifile.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/8 下午 1:44   hello      1.0         None

'''

import xlwings as xw

app = xw.App(visible=False, add_book=False)
for i in range(1, 3):
    # 添加一个工作簿，相当于一个 Excel 文档
    wb = app.books.add()
    # 文件名
    file_name = f'新建文件{i}.xlsx'
    # 保存文件
    wb.save(file_name)

# 选择第一个新建的工作簿，下标是从 0 开始的
wb = app.books[0]
sht = wb.sheets[0]
# 给A1单元格赋值
sht.range('A1').value = 'test1'
wb.save()
app.quit()

