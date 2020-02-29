#/usr/bin/python
# -*- coding:utf-8 -*-
'''
    作者:xguo
    文件:which_day_v1.0.py
    版本:v1.0
    日期:2019/2/25 15:10
    功能:
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

    days_in_month_tup = [31,28,31,30,31,30,31,31,30,31,30,31]
    # print(days_in_month_tup[:month - 1])

    # print(sum_days)
    # if (year % 400 == 0) or (year % 4 == 0 ) and (year % 100 != 0 ) :
    #     if month > 2:
    #         sum_days += 1

    if is_leap_year(year):
        days_in_month_tup[1] = 29
    sum_days = sum(days_in_month_tup[:month - 1]) + day
    print('这是第{}天'.format(sum_days))

if __name__ == "__main__":
    main()