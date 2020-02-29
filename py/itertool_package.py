#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:itertool_package.py
    功能:
    版本:1.0
    日期:2019/2/18 9:40
'''

from itertools import *


def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"


def main():
    c = count(4, 2)
    # for i in c:
    #     print(i)
    # print()
    # print(cycle('abc'))
    # print(repeat(1.2, 5))
    #
    # rlt = starmap(pow, [(1, 1), (2, 2), (3, 3)])
    # print(rlt)

    friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]

    friends = sorted(friends, key=height_class)
    for m, n in groupby(friends, key=height_class):
        print(m)
        print(list(n))


if __name__ == '__main__':
    main()
