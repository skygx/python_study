# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   workday_1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/1/3 下午8:09   hello      1.0         None

'''
import datetime
import chinese_calendar
import sys
import calendar
import workalendar
from dateutil.rrule import rrule, DAILY, MO, WE, FR, TH, SA, SU,TU
from dateutil.relativedelta  import relativedelta

# 节假日
off_workdays = {
    '20250101': '元旦',
    '20250128': '春节',
    '20250129': '春节',
    '20250130': '春节',
    '20250131': '春节',
    '20250201': '春节',
    '20250202': '春节',
    '20250203': '春节',
    '20250204': '春节',
    '20250404': '清明',
    '20250405': '清明',
    '20250406': '清明',
    '20250501': '五一',
    '20250502': '五一',
    '20250503': '五一',
    '20250504': '五一',
    '20250505': '五一',
    '20250531': '端午',
    '20250601': '端午',
    '20250602': '端午',
    '20251001': '国庆',
    '20251002': '国庆',
    '20251003': '国庆',
    '20251004': '国庆',
    '20251005': '国庆',
    '20251006': '国庆',
    '20251007': '国庆',
    '20251008': '国庆',
}
# 周末上班日
on_workdays = {
    '20250126': '春节',
    '20250208': '春节',
    '20250407': '清明',
    '20250427': '五一',
    '20250928': '国庆',
    '20251011': '国庆',
}
def is_workday(date):
    """
    判断是否为工作日
    :param date: 日期
    :return: True/False
    """
    if date.strftime('%Y') in ['2025']:
        if date.strftime('%Y%m%d') in on_workdays or ( date.weekday() <5 and date.strftime('%Y%m%d') not in off_workdays):
            return True
        else:
            return False
    else:
        if chinese_calendar.is_workday(date):
            return True
        else:
            return False

def workday_count(start_date, end_date):
    """
    计算工作日数量
    :param start_date: 开始日期
    :param end_date: 结束日期
    :return: 工作日数量
    """
    # print(start_date, end_date)
    if isinstance(start_date, str):
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    if isinstance(end_date, str):
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    count = 0

    while start_date <= end_date:
        if is_workday(start_date):
            count += 1
        # print(start_date, is_workday(start_date))
        start_date += datetime.timedelta(days=1)
    return count
def main():
    # start_date = sys.argv[1]
    # end_date = sys.argv[2]
    start_date = '2024-12-21'
    end_date = '2025-01-20'
    print("workday count:", workday_count(start_date, end_date))

if __name__ == '__main__':
    main()
