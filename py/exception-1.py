#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:exception-1.py
    功能:利用递归绘制分形树
    版本:1.0
    日期:2019/11/2419:19
'''


def main():
    while True:
        try:
            x=int(input("Enter the first number: "))
            y=int(input("Enter the second number: "))
            value=x/y
            print('x /y is',value)
        except Exception as e:
            print('Invalid input:',e)
            print('Please try again')

        else:
            break


if __name__ == "__main__":
    main()