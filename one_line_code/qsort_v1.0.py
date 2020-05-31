#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   qsort_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/7 22:03   xguo      1.0         None

'''


def main():
    qsort = lambda arr:len(arr)>1 and qsort(list(filter(lambda x:x<=arr[0],arr[1:]))) + arr[0:1] + qsort(list(filter(lambda x:x>arr[0],arr[1:]))) or arr
    l = [2,3,1,7,4,9]
    print(qsort(l))



if __name__ == "__main__":
    main()