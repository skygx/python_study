# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   python_study
    @File    :   excel2json.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/10/30 下午4:42   hello      1.0         None

'''
import pandas as pd
from pprint import pprint
import json
def excel_to_json(file):
    data = pd.read_excel(file)
    r = data.to_json(orient='records')
    return r

if __name__ == '__main__':
    file='../data/list.xlsx'
    pprint(json.loads(excel_to_json(file)))
