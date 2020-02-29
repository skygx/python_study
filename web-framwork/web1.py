#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   web1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/2  15:49   xguo      1.0         None

'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello world"}
