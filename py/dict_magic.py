#/usr/bin/python
# -*- coding:utf-8 -*-
'''
    作者:xguo
    文件:dict_magic.py
    版本:v1.0
    日期:2019/2/25 15:38
    功能:
'''


def main():
    my_dict = {'cc':100,'aa':200,'bb':10}
    print(sorted(my_dict.items(),key=lambda x:x[0]))
    print(sorted(my_dict.items(),key=lambda x:x[1]))
    print(my_dict.get('dd','Not found'))

    good_score = {name:score for name,score in my_dict.items() if score > 90}
    print(good_score)

    dict_reverse = dict(zip(my_dict.values(),my_dict.keys()))
    print(dict_reverse)


if __name__ == "__main__":
    main()