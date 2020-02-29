#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:bmr_v1.0.py
    功能:输入参数，输出BMR基准体脂率
    版本:1.0
    日期:2019/2/21 15:49
'''


def main():

    gender = input("性别：")
    # print(type(gender))

    weight = float(input("体重(kg)："))
    # print(type(weight))

    height = float(input("身高(cm)："))
    # print(type(height))

    age = float(input("年龄："))
    # print(type(age))

    if gender == '男':
        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66.0
    elif gender == '女':
        bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655.0
    else:
        bmr = -1

    if bmr != -1:
        print("基准代谢率为（大卡）：", bmr)
    else:
        print("不存在此性别")


if __name__ == "__main__":
    main()