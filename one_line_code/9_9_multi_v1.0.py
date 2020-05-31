#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   9_9_multi_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/7 21:54   xguo      1.0         None

'''


def main():
    print('\n'.join([' '.join(['%s*%s=%-2s'%(y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))


if __name__ == "__main__":
    main()