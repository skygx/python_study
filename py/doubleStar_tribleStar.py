#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   doubleStar_tribleStar.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/2/27 20:46   xguo      1.0         None

'''
from random import randint

def transpose_list(list_of_list):
    '''

    :param list_of_list:
    :return:
    '''
    return [list(row) for row in zip(*list_of_list)]

def roll(*dice):
    '''

    :param dice:
    :return:
    '''
    return sum(randint(1,d) for d in dice)

def tag(tag_name,**attributes):
    '''

    :param tag_name:
    :param attributes:
    :return:
    '''
    attributes_list = [f'{name}="{value}"' for name,value in attributes.items()]
    return f'<{tag_name} {" " .join(attributes_list)}>'

def with_previous(iterable,*,fillvalue=None):
    '''

    :param iterable:
    :param fillvalue:
    :return:
    '''
    previous = fillvalue
    for item in iterable:
        yield previous,item
        previous = item

def palindromify(sequence):
    '''

    :param sequence:
    :return:
    '''
    return [*sequence,*reversed(sequence)]

def main():
    #list unpack
    nums = [2,3,4,1,6,9]
    more_nums = [*nums,11,22]
    print(*more_nums)

    #transform list
    l = [[1,4,7],[2,5,8],[3,6,9],[10,11,12]]
    print(transpose_list(l))

    #roll
    print(roll(20))
    print(roll(6,6))
    print(roll(6,6,6))

    #html tag
    print(tag('a',href='http://www.baidu.com'))
    print(tag('img',height=20,width=40,src='face.jpg'))

    #previouse iterable
    #fillvalue  keyword arguement   with_previous([2,3,4],0) is wrong
    print(list(with_previous([2,5,3,8,3],fillvalue=1)))

    #seq and reverse seq
    s = [1,2,3,4,5]
    print(palindromify(s))

if __name__ == "__main__":
    main()