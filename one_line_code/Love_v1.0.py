#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   Love_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/7 21:31   xguo      1.0         None

'''


def main():
    print('\n'.join([' '.join([('Love'[(x-y)%len('Love')] if (((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0) else ' ') for x in range(-30,30)])for y in range(30,-30,-1)]))


if __name__ == "__main__":
    main()