#/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Project :   Pyproject
    @File    :   starlette_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/1/12 下午 2:50   hello      1.0         None

"""

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from anyio import Path

async def file(request):
    text = await Path('demo.txt').read_text()
    return JSONResponse(text)

app = Starlette(debug=True, routes=[Route('/file', file),])
