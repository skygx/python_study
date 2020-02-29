#/usr/bin/python
# -*- coding:utf-8 -*-
'''
    作者:xguo
    文件:52week_money_challenge.py
    版本:v1.0
    日期:2019/2/25 14:37
    功能:查看52周累计金额
'''
import datetime
import math

def save_money_in_n_weeks(money_per_week,increase_money,total_week):
    money_list = []
    saving_list = []
    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        print('第{}周，存入{}元，账户累计{}元'.format(i + 1,money_per_week, saving))
        money_per_week += increase_money
        saving_list.append(saving)

    return saving_list

def main():
    money_per_week = float(input('请输入每周的存入的金额：'))
    increase_money = float(input('请输入每周的递增金额：'))
    total_week = int(input('请输入总共的周数：'))

    saved_money_list = save_money_in_n_weeks(money_per_week,increase_money,total_week)
    input_date_str = input("请输入日期(yyyy/mm/dd)：")
    input_date = datetime.datetime.strptime(input_date_str, "%Y/%m/%d")
    week_num = input_date.isocalendar()[1]
    print('第{}周的存款：{}元'.format(week_num,saved_money_list[week_num - 1]))

if __name__ == "__main__":
    main()