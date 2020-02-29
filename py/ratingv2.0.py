#/usr/bin/python
# -*- coding:utf-8 -*-
'''
    作者:xguo
    文件:rating.py
    功能:人名币和美元汇率兑换
    版本:2.0
    日期:2019/2/18 8:47
    新增：将汇率兑换模块化
'''

RMB_VS_USD = 6.77


def convert_currency(im, er):
    out = im * er
    return out


def main():
    currency_str_value = input("请输入带单位的货币金额:")
    unit = currency_str_value[-3:]
    if unit == 'CNY':
        exchange_rate = 1 / RMB_VS_USD
    elif unit == 'USD':
        exchange_rate = RMB_VS_USD
    else:
        exchange_rate = -1
    if exchange_rate != -1:
        currency_value = eval(currency_str_value[:-3])
        convert_currency2 = lambda x: x * exchange_rate
        # currency = convert_currency(currency_value,exchange_rate)
        currency = convert_currency2(currency_value)
        print("金额：", currency)
    else:
        print("不支持此货币")


if __name__ == '__main__':
    main()
