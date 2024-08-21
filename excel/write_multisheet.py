#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   write_multisheet.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/8 下午 1:49   hello      1.0         None

'''

import xlwings as xw

app = xw.App(visible=False, add_book=False)
# 打开工作簿
wb = app.books.open('./新建文件2.xlsx')

for i in range(1, 6):
    # 工作表的名称
    sht_name = f'sheet_{i}'
    # 新增一个工作表
    sht = wb.sheets.add(sht_name)

# 在最后一个新建的工作表中写入内容
wb.sheets[0].range('B2:C3').value = [[1, 3],
                                     [2, 4]]
wb.save()
app.quit()
