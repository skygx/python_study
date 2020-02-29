#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:17_tips.py
    功能:
    版本:1.0
    日期:2019/2/19 22:36
'''


from collections import Counter


def product(a, b):
    return a * b


def add(a, b):
    return a + b


def minIndex(lst):
    return min(range(len(lst)), key=lst.__getitem__)


def maxIndex(lst):
    return max(range(len(lst)),key=lst.__getitem__)


def main():
    a = [1,2,3,1,2,3,2,2,4,5,1]
    print(max(set(a),key=a.count))
    cnt = Counter(a)
    print(cnt.most_common(3))

    str1 = 'hello'
    str2 = 'loleh'
    print(Counter(str1) == Counter(str2))

    a = 'abcdefghijk'
    print(a[::-1])
    print(list(reversed(a)))

    original = [['a', 'b'],['c', 'd'], ['e', 'f']]
    transfer = zip(*original)
    print(list(transfer))

    b = 6
    print(4<b<7)
    print(1 == b < 7)

    b = True
    print((product if b else add)(5,7))

    lst = [40,10,20,30,60,-5]
    print(minIndex(lst))
    print(maxIndex(lst))


if __name__ == "__main__":
    main()
