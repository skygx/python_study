#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   date-format.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/1  13:29   xguo      1.0         None

'''

_formats={
    'ymd':'{d.year}-{d.month}-{d.day}',
    'mdy':'{d.month}/{d.day}/{d.year}',
    'dmy':'{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def __format__(self, code):
        if code == '':
            code='ymd'
        fmt=_formats[code]
        return fmt.format(d=self)

def main():
    d=Date(2012,12,21)
    print(format(d))
    print(format(d,'mdy'))
    print('The date is {:ymd}'.format(d))
    print('The date is {:dmy}'.format(d))

if __name__ == "__main__":
    main()