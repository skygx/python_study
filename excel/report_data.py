#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   report_data.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/22 下午 1:36   hello      1.0         None

'''
import sweetviz as sv  # 导入sweetviz库，如同拔出藏于剑鞘的利剑
import pandas as pd  # 导入pandas库，掌握数据处理的要诀

# 加载数据，如同武侠小说中的英雄踏上征程
# data = pd.read_csv("../city_aqi.csv")
data = pd.read_csv("../data/test.csv")
# data = pd.read_excel("../学生信息表.xlsx")

# 使用Sweetviz分析数据，如同探索未知的江湖
report = sv.analyze(data)

# 生成报告，如同绘制出一幅江湖地图
report.show_html("Sweetviz_Report.html")
