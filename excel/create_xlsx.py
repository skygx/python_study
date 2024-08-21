#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   create_xlsx.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/8 上午 9:02   hello      1.0         None

'''

import xlwings as xw

def create_xlsx(file_path):
    """1、创建 xlsx 表格并写入数据"""
    std_array = [['学生编号', '学生姓名', '出生日期', '班级编号', '性别', '籍贯'],
                ['0001', '张三', '1990/12/5', '1001', '男', '广东'],
                ['0002', '李四', '1991/2/25', '1001', '女', '山东'],
                ['0003', '王五', '1991/8/16', '1002', '男', '江苏'],
                ['0004', '赵六', '1992/6/21', '1002', '女', '内蒙古']]
	# 开启 Excel 应用，参数visible表示处理过程是否可视，如果add_book为False则代表默认不创建空白工作簿
    app = xw.App(visible=False, add_book=False)
    # 添加工作簿，相当于一个Excel文档
    wb = app.books.add()
    # 添加名为'学生信息表'的sheet，准备写入数据
    sheet = wb.sheets.add('学生信息表')
    # 在单元格A1中开始写入数组
    sheet.range('A1').value = std_array
    # 保存工作簿
    wb.save(file_path)
    # 关闭工作簿
    wb.close()
    # 退出 Excel 编辑应用
    app.quit()

if __name__ == "__main__":
    file_path = './学生信息表.xlsx'
    create_xlsx(file_path)
