#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   distance_two_points.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/1  10:24   xguo      1.0         two pornts distance

'''

import math
from functools import partial

def distance(p1,p2):
    x1, y1=p1
    x2, y2=p2
    return math.hypot(x2-x1, y2-y1)

def main():
    points=[(1,2),(3,4),(5,6),(7,8)]
    pt=(4,3)
    points.sort(key=partial(distance, pt))
    print(points)

if __name__ == "__main__":
    main()