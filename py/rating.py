#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:rating.py
    功能:
    版本:1.0
    日期:2019/2/18 8:47
'''

RMB_VS_USD = 6.7

def main():
    rmb_str_value = input("请输入金额（CNY）:")
    rmb_value = eval(rmb_str_value)
    usd_value = rmb_value / RMB_VS_USD
    print("美元金额：",usd_value)

if __name__ == '__main__':
    main()