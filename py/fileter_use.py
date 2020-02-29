#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者：xguo
    文件：fileter_use.py
    版本：v1.0
    日期：2019/3/1 20:25
    功能：
'''
import re

def main():
    options = {'code': 'utf8'}
    base = {'name': 'xguo', 'sex': 'male'}
    print(dict(base, **options))
    # print(base)
    base.update(options)
    print(base)

    print({x: y for x in range(4) for y in range(10)})

    list1 = ['to_pickle', 'to_record', 'to_sparse', 'to_sql', 'to_state', 'to_string', 'to_timestamp', 'update',
             'update_sql']
    print(list(filter(lambda x: str(x).startswith('update'), list1)))
    print(list(filter(lambda x: re.findall('to_', x), list1)))
    list2 = [{'aa': 1, 'bb': 2}]
    print(list(filter(lambda x: 'aa' in x.keys(), list2)))


if __name__ == "__main__":
    main()