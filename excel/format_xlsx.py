#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   format_xlsx.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/8 下午 1:38   hello      1.0         None

'''

from datetime import datetime
import xlwings as xw

def format_test():
    """设置单元格的格式"""
    apps = xw.App(visible=False, add_book=False)
    wb = apps.books.add()
    sheet = wb.sheets.add('字体')
    cell_A1 = sheet.range('A1')
    cell_A1.value = '字符串'

    # 获取单元格的字体属性
    font_name = cell_A1.api.Font.Name	# 获取字体名称
    font_size = cell_A1.api.Font.Size	# 获取字号
    font_bold = cell_A1.api.Font.Bold	# 获取是否加粗，True表示加粗，False表示不加粗
    font_color = cell_A1.api.Font.Color	# 获取字体颜色
    print(f'字体: {font_name}, 字号: {font_size}, 加粗: {font_bold}, 颜色: {font_color}')

    # 设置字体属性
    cell_A1.api.Font.Name = '华文仿宋'	# 设置字体：华文仿宋
    cell_A1.api.Font.Size = 15			# 设置字号为15
    cell_A1.api.Font.Bold = True		# 加粗
    cell_A1.api.Font.Color = 0x0000FF	# 设置为红色RGB（255,0，0）
    # 添加下划线
    cell_A1.api.Font.Underline = 2
    # 金额(数字)格式化
    cell_B1 = sheet.range('B1')
    cell_B1.value = 3000000
    cell_B1.api.NumberFormat = '￥#,###.00'
    # 水平方向对齐方式：-4108 居中, -4131 靠左, -4152 靠右
    cell_B1.api.HorizontalAlignment = -4152
	# 日期格式化
    cell_C1 = sheet.range('C1')
    date = datetime.today()
    cell_C1.value = date
    cell_C1.api.NumberFormat = 'yyyy-mm-dd hh:MM:ss'
    cell_C1.api.HorizontalAlignment = -4108
    # 垂直方向对齐方式: -4108 居中(默认), -4160 靠上, -4107 靠下, -4130 自动换行对齐
    cell_C1.api.VerticalAlignment = -4107

    wb.save('格式化测试.xlsx')
    wb.close()
    apps.quit()


if __name__ == "__main__":
    format_test()
