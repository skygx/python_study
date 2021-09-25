#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   scheduler_job.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/21  10:59   xguo      1.0         None

'''
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

scheduler = BackgroundScheduler()
scheduler.start()

@scheduler.scheduled_job('interval',seconds=3)
def print_str():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def main():
    while True:
        if input('please input:') == 'quit':
            break

if __name__ == "__main__":
    main()