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
2019/3/2 7:30     xguo      3.0         添加PasswordTool,FileTool封装类
'''

class PasswordTool:

    def __init__(self,password):
        self.password = password
        self.strengh_level = 0

    def check_number_exist(self):
        has_numeric = False
        for i in self.password:
            if i.isnumeric():
                has_numeric = True
                break
        return has_numeric

    def check_alpha_exist(self):
        has_letter = False
        for i in self.password:
            if i.isalpha():
                has_letter = True
                break
        return has_letter

    def process_check(self):
        # 规则1：密码长度大于8
        if len(self.password) >= 8:
            self.strengh_level += 1
        else:
            print("密码长度不足8位")
        # 规则2：密码中包含数字
        if self.check_number_exist():
            self.strengh_level += 1
        else:
            print ("密码中不包含数字")

        # 规则3：密码中包含字母
        if self.check_alpha_exist():
            self.strengh_level += 1
        else:
            print ("密码中不包含字母")

        return self.strengh_level

class FileTool:
    def __init__(self,filepath):
        self.filepath = filepath

    def write_file(self,line):
        # 每次密码都写入文件
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines

def main():


    try_times = 5
    filepath = r'password.txt'
    filetool = FileTool(filepath)

    while try_times > 0 :
        password = input("请输入密码：")
        # 密码强度
        pwdtool = PasswordTool(password)
        strengh_level = pwdtool.process_check()

        filetool.write_file(f'密码：{password} 强度：{strengh_level}\n')

        #判断密码是否是强密码
        if strengh_level == 3:
            print ("这是一个强密码")
            break
        else:
            try_times -= 1
            print (f"这是一个弱密码,还可以输入{try_times}")

    if try_times != 0:
        print("密码输入结束")

    lines = filetool.read_file()
    for l in lines:
        print (l)

if __name__ == "__main__":
    main()