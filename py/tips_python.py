#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者：xguo
    文件：tips_python.py
    版本：v1.0
    日期：2019/3/1 20:06
    功能：
'''
from itertools import combinations
from collections import Counter
import heapq

def main():
    lst = ['xguo','shen','li','yao']
    print(list(combinations(lst,2)))

    itm = [0] + [1] + [2,3]
    itm1 = [0] * 4
    print(itm)
    print(itm1)

    nums = [1,2,3,2,3,4,11,6,5]
    num_set = set(nums)
    print(max(set(nums),key=nums.count))
    print(Counter(nums).most_common(1))
    print(heapq.nlargest(2,num_set))
    print(heapq.nsmallest(3,num_set))
    students = [
        {'name':'AA','score':100,'height':189} ,
        {'name':'BB','score':10,'height':179} ,
        {'name':'CC','score':60,'height':169} ,
    ]
    print(heapq.nlargest(2,students,key=lambda x:x['height']))
    print(heapq.nlargest(2,students,key=lambda x:x['score']))

    print(isinstance(1,(int,str)))


if __name__ == "__main__":
    main()