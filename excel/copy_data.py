#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   copy_data.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/8 下午 2:38   hello      1.0         None

'''

import xlwings as xw

app = xw.App(visible=False, add_book=False)

# 打开第一个工作簿
filepath1 = './新建文件2.xlsx'
wb1 = app.books.open(filepath1)
# 选择工作表
sht1 = wb1.sheets[0]
# 需要复制的内容
content = sht1.range('B2:C3').value
# 新建工作表，用于存放复制的内容
new_sht = wb1.sheets.add('复制内容')
# 填入复制的内容
new_sht.range('B2').value = content
wb1.save(filepath1)
wb1.close()

# 打开第二个Excel文档
filepath2 = './新建文件3.xlsx'
wb2 = app.books.open(filepath2)
sht2 = wb2.sheets[0]
sht2.range('B2:C3').value = content
wb2.save(filepath2)
wb2.close()
app.quit()
