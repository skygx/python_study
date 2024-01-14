#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   qrcode_make.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/2/25 下午 8:33   hello      1.0         None

'''

import qrcode

img = qrcode.make('https://mp.weixin.qq.com/s/ijEPwIIrLZo_BykYHcVWGw')

img.save('./pic.jpg')
