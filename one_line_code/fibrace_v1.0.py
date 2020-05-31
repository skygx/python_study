#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   fibrace_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/7 22:01   xguo      1.0         None

'''


def main():
    print([x[0] for x in [(a[i][0],a.append([a[i][1],a[i][0]+a[i][1]]))for a in ([[1,1]],)for i in range(30)]])


if __name__ == "__main__":
    main()