#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   QR-code.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/26  9:42   xguo      1.0         None

'''

from MyQR import myqr

def main():
    myqr.run(words='http://www.baidu.com',
             save_name='code.jpg')



if __name__ == "__main__":
    main()