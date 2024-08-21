#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   read_multifile.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/8 下午 1:45   hello      1.0         None

'''

import xlwings as xw

app = xw.App(visible=False, add_book=False)
for i in range(1, 3):
    # 文件名
    file_name = f'新建文件{i}.xlsx'
    # 打开工作簿
    wb = app.books.open(file_name)

    # 选择第一个新建的工作簿
wb = app.books[0]
# 选择该工作簿的工作表
sht = wb.sheets[0]
# 获取A1单元格的值
val = sht.range('A1').value
print(val)

wb.save()
app.quit()

