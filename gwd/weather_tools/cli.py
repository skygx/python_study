# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   cli.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/18 上午9:34   hello      1.0         None

'''
import sys
from weather_tools.fetcher import get_weather
from weather_tools.parser import parse_weather
from weather_tools.formatter import format_output

# if len(sys.argv) != 2:
#     print("Usage: python cli.py <city>")
#     sys.exit(1)

def main(city="beijing"):
    # city = "beijing"
    data = get_weather(city)
    location, temp_c, condition = parse_weather(data)
    output = format_output(location, temp_c, condition)
    print(output)

# city = sys.argv[1]
if __name__ == '__main__':
    main("new york")

# city = "beijing"
# data = get_weather(city)
# location, temp_c, condition = parse_weather(data)
# output = format_output(location, temp_c, condition)
# print(output)
