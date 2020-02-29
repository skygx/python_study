#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者：xguo
    文件：min_max_Index_v1.0.py
    版本：v1.0
    日期：2019/3/1 19:55
    功能：
'''


def minIndex(lst:list):
    return min(range(len(lst)),key=lst.__getitem__)

def maxIndex(lst:list):
    return max(range(len(lst)),key=lst.__getitem__)

def main():
    lst = [40,10,20,30,5]
    print(maxIndex(lst))
    print(minIndex(lst))

if __name__ == "__main__":
    main()