# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   formatter.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/18 上午9:33   hello      1.0         None

'''
def format_output(location, temp_c, condition):
    """Format weather information into a readable string."""
    return f"Weather in {location}: {temp_c}°C, {condition}"
