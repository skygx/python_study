#/usr/bin/python
# -*- coding:utf-8 -*-
'''
    作者:xguo
    文件:which_day_v1.0.py
    版本:v3.0
    日期:2019/2/25 15:10
    功能:输入年月日显示这年的第几天
    新增2:用集合表示30天，31天月份
    新增3:用字典表示月对应天数
    新增4：strftime()函数直接获取第几天
'''
from datetime import datetime
import time


def is_leap_year(year):
    '''

    :param year:
    :return: true if leap year
             false if not leap year
    '''
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

    # _30_days_month_set = {4,6,9,11}
    # _31_days_month_set = {1,3,5,7,8,10,12}

    month_dict_days = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }

    days_month_dict = {
        30:{4,6,9,11},
        31:{1,3,5,7,8,10,12}
    }

    days = 0
    days += day

    for i in range(1,month):
        days += month_dict_days[i]

    if is_leap_year(year) and month > 2:
        days += 1

    print('这是第{}天'.format(days))
    # print(datetime.now().strftime('%j'))
    print(input_date.strftime('%j'))

if __name__ == "__main__":
    main()