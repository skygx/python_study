#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   async_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/1/12 下午 2:29   hello      1.0         None

'''

from aiohttp import web
import aiofiles

routes = web.RouteTableDef()

@routes.get("/file")
async def file(request):
    async with aiofiles.open("demo.txt") as fp:
        text = await fp.read()
    return web.Response(text=text)

if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
