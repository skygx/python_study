# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/1/6 下午1:46   hello      1.0         None

'''
from plombery import register_pipeline,task,get_logger,get_app,Trigger
from apscheduler.triggers.interval import IntervalTrigger
import time
from pydantic import BaseModel

class InputParams(BaseModel):
    name: str
@task
def say_hello(name:InputParams):
    # print(f"Hello, {name}!")
    get_logger().info(f"Hello, {name}!")
    time.sleep(3)

register_pipeline(id='test_pipeline',
                  name='test_pipeline',
                  description='test_pipeline',
                  tasks=[say_hello],
                  params=InputParams,

                  )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("plombery:get_app", reload=True,factory=True,reload_dirs="..")
