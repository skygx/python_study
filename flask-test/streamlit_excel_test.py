#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   streamlit_excel_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/28 下午 4:25   hello      1.0         None

'''

import streamlit as st
import pandas as pd

df = pd.read_excel(r"D:\project\Pyproject\python_study\flask-test\新核心主机.xls",sheet_name="北京生产地址")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.dataframe(df,height=None,width=860)
