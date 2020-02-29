#/usr/bin/python
# -*- coding:utf-8 -*-
'''
    作者:xguo
    文件:which_day_v1.0.py
    版本:v2.0
    日期:2019/2/25 15:10
    功能:输入年月日显示这年的第几天
    新增:用集合表示30天，31天月份
'''
from datetime import datetime
'''
    判断year是否为闰年
    是，返回true
    否，返回false
'''
def is_leap_year(year):
    is_leap = False
    if (year % 400 == 0) or (year % 4 == 0 ) and (year % 100 != 0 ) :
        is_leap = True
    return is_leap

def main():
    input_date_str = input('请输入日期(yyyy/mm/dd)：')
    input_date = datetime.strptime(input_date_str, "%Y/%m/%d")
    # print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # days_in_month_tup = [31,28,31,30,31,30,31,31,30,31,30,31]
    _30_days_month_set = {4,6,9,11}
    _31_days_month_set = {1,3,5,7,8,10,12}

    days = day

    for i in range(1,month):
        if i in _30_days_month_set:
            days += 30
        elif i in _31_days_month_set:
            days += 31
        else:
            days += 28

    if is_leap_year(year) and month > 2:
        days += 1

    print('这是第{}天'.format(days))

if __name__ == "__main__":
    main()