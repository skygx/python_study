#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   wide_height.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/8 下午 1:43   hello      1.0         None

'''

import xlwings as xw

app = xw.App(visible=False)
# 新添加Excel文档
wb = app.books.add()
sht = wb.sheets['Sheet1']
# 设置高度和宽度
cell = sht.range('A1')
cell.column_width = 60
cell.row_height = 35
# 设置字体
cell.api.Font.Name = '黑体' # 设置字体：黑体
cell.api.Font.Size = 30
cell.api.Font.Bold = True
cell.api.Font.Color = 0xFF00FF
cell.api.HorizontalAlignment = -4108
cell.value = '人生苦短，我用Python'

wb.save('./高度和宽度.xlsx')
wb.close()
app.quit()
