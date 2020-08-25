#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   30_simple_instance.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/28  20:33   xguo      1.0         None

'''

from collections import Counter
import sys
from math import ceil
import re
from re import sub
from copy import deepcopy
from random import randint


def shuffle(lst):
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while (m):
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst

def chunk(lst,size):
    return list(map(lambda x:lst[x * size:x * size + size], list(range(0,ceil(len(lst) / size)))))
def anagram(first, second):
    return Counter(first) == Counter(second)

def all_unique(lst):
    return len(lst)== len(set(lst))

def byte_size(string):
    return(len(string.encode('utf-8')))

def compact(lst):
    return list(filter(bool,lst))


def count_vowels(str):
    return len(re.findall(r'[aeiou]',str,re.IGNORECASE))

def spread(arg):
    ret=[]
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(lst):
    result=[]
    result.extend(spread(list(map(lambda x: deep_flatten(x) if type(x)==list else x,lst))))
    return result

def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison_a = set_a.difference(set_b)
    comparison_b = set_b.difference(set_a)
    return [list(comparison_a),list(comparison_b)]

def has_duplicates(lst):
    return len(lst) != len(set(lst))

def merge_two_dicts(a,b):
    c = a.copy()
    c.update(b)
    return c

def merge_dictionaries(a, b):
    return {**a, **b}

def most_frequent(list):
    return max(set(list), key=list.count)

def palindrome(str):
    s = sub('[\W_]', '', str.lower())
    return s == s[::-1]

def main():
    x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
    y = [1, 2, 3, 4, 5]
    print('all_unique'.center(50, '-'))
    print(all_unique(x))  # False
    print(all_unique(y))  # True
    print('anagram'.center(50,'-'))
    print(anagram('3abc','a3bc'))
    print('memory use'.center(50,'-'))
    value=30
    print(sys.getsizeof(value))
    print('byte size'.center(50,'-'))
    print(byte_size(' '))
    print(byte_size('hello world'))
    print('chunk'.center(50,'-'))
    print(chunk([1,2,3,4,5,6,7,8,9],2))
    print('compact'.center(50,'-'))
    print(compact([0,1,False,2,' ',3,'a','s',None,34,'\n']))

    print('unzip'.center(50,'-'))
    array=[['a',1],['b',2],['c',4],[5,'d']]
    transposed=list(zip(*array))
    print(transposed)

    print('count vowels'.center(50,'-'))
    print(count_vowels('foobar'))
    print(count_vowels('gymist'))

    print('spread list'.center(50,'-'))
    print(deep_flatten([1,[2],[[3],4],5]))

    print('list difference'.center(50,'-'))
    print(difference([1,2,3],[2,3,4]))

    print('has duplicates'.center(50,'-'))
    x = [1,2,3,4,5,5]
    y = [2,3,4,5]
    print(has_duplicates(x))
    print(has_duplicates(y))

    print('has duplicates'.center(50,'-'))
    a = {'x':1,'y':2}
    b = {'y':3,'z':4}
    print(merge_two_dicts(a,b))
    print(merge_dictionaries(a,b))

    print('most frequent'.center(50,'-'))
    lst = [1,2,1,2,3,2,1,4,2]
    print(most_frequent(lst))

    print('most frequent'.center(50,'-'))
    str = 'taco cat'
    print(palindrome(str))

    print('shuffle'.center(50,'-'))
    foo = [1,2,3]
    print(shuffle(foo))


if __name__ == "__main__":
    main()