#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者：xguo
    文件：list_embed_fold.py
    版本：v1.0
    日期：2019/2/26 22:02
    功能：
'''
import re

def main():
    l = [1, 2, [3, [5, 6, [7, 8]]]]
    flat = lambda x : sum(map(flat, x), []) if isinstance(x, list) else [x]
    print(flat(l))
    flatten = lambda x:[y for i in x for y in flatten(i)] if type(x) is list else [x]
    print(flatten(l))

if __name__ == "__main__":
    main()