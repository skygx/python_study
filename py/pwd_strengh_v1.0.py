#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   pwd_strengh_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/27 15:23   xguo      1.0         输入密码判断强弱密码

'''

def check_number_exist(password):
    for i in password:
        if i.isnumeric():
            return True
    return False

def check_alpha_exist(password):
    for i in password:
        if i.isalpha():
            return True
    return False

def main():

    password = input("请输入密码：")
    #密码强度
    strengh_level = 0

    #规则1：密码长度大于8
    if len(password) >= 8:
        strengh_level += 1
    else:
        print("密码长度不足8位")
    #规则2：密码中包含数字
    if check_number_exist(password):
        strengh_level += 1
    else:
        print ("密码中不包含数字")

    #规则3：密码中包含字母
    if check_alpha_exist(password):
        strengh_level += 1
    else:
        print ("密码中不包含字母")

    if strengh_level == 3:
        print ("这是一个强密码")
    else:
        print ("这是一个弱密码")

if __name__ == "__main__":
    main()