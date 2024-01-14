#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   streamlit_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/1/11 上午 11:33   hello      1.0         None

'''

import streamlit as st
import pandas as pd

read_and_cache_csv=st.cache(pd.read_csv)

st.write("""
# My first app
Hello *world!*
""")

x = st.slider('x')
st.write(x, 'squared is', x * x)

BUCKET="https://streamlit-self-driving.s3-us-west-2.amazonaws.com/"
data=read_and_cache_csv(BUCKET + "labels.csv.gz",nrows=1000)
desired_label = st.selectbox('Filter to:', ['car','truck'])
st.write(data[data.label == desired_label])
