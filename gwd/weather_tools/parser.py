# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   parser.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/18 上午9:33   hello      1.0         None

'''
def parse_weather(data):
    """Parse weather data to extract relevant information."""
    location = data['location']['name']
    temp_c = data['current']['temp_c']
    condition = data['current']['condition']['text']
    return location, temp_c, condition
