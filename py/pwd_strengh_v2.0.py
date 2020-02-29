#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   pwd_strengh_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/27 15:23   xguo      1.0         输入密码判断强弱密码
2019/2/28 13:04   xguo      2.0         循环指定次数输入密码，并将输入密码写入文件

'''

def check_number_exist(password):
    has_numeric = False
    for i in password:
        if i.isnumeric():
            has_numeric = True
            break
    return has_numeric

def check_alpha_exist(password):
    has_letter = False
    for i in password:
        if i.isalpha():
            has_letter = True
            break
    return has_letter

def main():


    try_times = 5

    while try_times > 0 :
        password = input("请输入密码：")
        # 密码强度
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

        #每次密码都写入文件
        f = open(r"E:\project\python\python_study\python_study\password.txt",'a')
        f.write(f'密码：{password} 强度：{strengh_level}\n')
        f.close()

        #判断密码是否是强密码
        if strengh_level == 3:
            print ("这是一个强密码")
            break
        else:
            try_times -= 1
            print (f"这是一个弱密码,还可以输入{try_times}")



    if try_times != 0:
        print("密码输入结束")

if __name__ == "__main__":
    main()