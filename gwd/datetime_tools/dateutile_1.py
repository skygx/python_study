# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   dateutile_1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/18 上午10:54   hello      1.0         None

'''
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
from datetime import datetime
from dateutil import parser, tz

def next_weekday(date, weekday):
    """获取下一个指定星期几的日期"""
    days_ahead = weekday - date.weekday()
    if days_ahead <= 0:  # 如果目标星期几已过，则查找下周
        days_ahead += 7
    return date + relativedelta(days=days_ahead)
def parse_date(date_string):
    # date_string = "2023年4月1日 14:30:00"
    parsed_date = parser.parse(date_string, fuzzy=True,dayfirst=False,yearfirst=False)
    print(parsed_date)

def get_local_time():
    local_time=datetime.now(tz.tzlocal())
    utc_time=local_time.astimezone(tz.tzutc())
    print(f"本地时间:{local_time}")
    print(f"UTC时间:{utc_time}")

def cal_time():
    now=datetime.now()
    three_months_later=now+relativedelta(months=3)
    print(f"三个月后:{three_months_later}")

# def get_next_friday():
#     date = parse("2024-09-18")  # 假设今天是2023年5月1日（星期一）
#     next_friday = next_weekday(date, 4)  # 4代表星期五
#     print(f"下一个星期五是: {next_friday.strftime('%Y-%m-%d')}")

def next_weekday(date, weekday):
    """获取下一个指定星期几的日期"""
    days_ahead = weekday - date.weekday()
    if days_ahead <= 0:  # 如果目标星期几已过，则查找下周
        days_ahead += 7
    next_day=date + relativedelta(days=days_ahead)
    print(f"下一个星期五是: {next_day.strftime('%Y-%m-%d')}")
    return next_day

if __name__ == '__main__':
    parse_date("2023年4月1日 14:30")
    get_local_time()
    cal_time()
    # get_next_friday()
    next_weekday(parse("2024-09-11"), 4)    #  4代表星期五

