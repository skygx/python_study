#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   write_to_xlsx.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/8 下午 1:34   hello      1.0         None

'''
import xlwings as xw

def write_to_Excel(file_path):
    """将数据写入Excel"""
    # 标题
    title = ['编号', '学号', '姓名', '科目', '年份', '分数']
    # 分数
    scores = [[1, 1, '张三', '数学', 2018, 98],
              [2, 1, '张三', '数学', 2019, 96],
              [3, 1, '张三', '数学', 2020, 96],
              [4, 1, '张三', '语文', 2018, 98],
              [5, 1, '张三', '语文', 2019, 92],
              [6, 1, '张三', '语文', 2020, 91],
              [7, 2, '李四', '语文', 2018, 85],
              [8, 2, '李四', '语文', 2019, 82],
              [9, 2, '李四', '语文', 2020, 84],
              [10, 2, '李四', '数学', 2018, 86],
              [11, 2, '李四', '数学', 2019, 88],
              [12, 2, '李四', '数学', 2020, 90]]
    apps = xw.App(visible=False, add_book=False)
    wb = apps.books.add()
    sheet = wb.sheets.add('分数')
    sheet.range('A1').value = title
    sheet.range('A2').value = scores

    wb.save(file_path)
    wb.close()
    apps.quit()


def write_to_Excel2():
    """其它的为单元格赋值的方法"""
    apps = xw.App(visible=False, add_book=False)
    wb = apps.books.add()
    sheet = wb.sheets.add('写入测试')

    # 写入一个列表
    sheet.range('A1').value = [1, 2, 3]
    # 从纵向写入一个列表
    sheet.range('A2').options(transpose=True).value = [4, 7]
    # 在 B2:C3单元格写入一个二维数组
    sheet.range('B2').value = [[5, 6],
                               [8, 9]]
    # 在单元格内写入 Excel 公式
    sheet.range('A4').formula = '=sum(A1:A3)'
    sheet.range('B4').formula = '=sum(B1:B3)'
    sheet.range('C4').formula = '=sum(C1:C3)'

    wb.save('./写入测试.xlsx')
    wb.close()
    apps.quit()

if __name__ == "__main__":
    file_path = './学生信息表.xlsx'
    file_path_score = './学生科目成绩表.xlsx'
    # read_xlsx(file_path)
    # get_cols_rows(file_path)
    # write_to_Excel(file_path_score)
    write_to_Excel2()
