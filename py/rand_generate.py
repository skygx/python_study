#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   rand_generate.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/7/8 10:18   xguo      1.0         None

'''
import random
import numpy as np

def main():
    ran = np.random.randint(1,100,5)
    print(ran)

if __name__ == "__main__":
    main()