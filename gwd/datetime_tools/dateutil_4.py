# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   dateutil_4.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/18 下午12:14   hello      1.0         None

'''
from dateutil.rrule import rrule, DAILY, MO, WE, FR, TH, SA, SU,TU
from datetime import datetime
from dateutil.relativedelta  import relativedelta

# 生成未来30天内的所有周一、周三和周五
start_date = datetime.now()
end_date = start_date + relativedelta(days=30)
weekdays = rrule(DAILY, dtstart=start_date, until=end_date, byweekday=(MO, WE, FR, TH, SA, SU, TU))
i=0
for date in weekdays:
    i=i+1
    print(date.strftime("%Y-%m-%d %A"))

print("weekdays:",i)
