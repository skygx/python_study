# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   config.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/26 下午3:52   hello      1.0         None

'''
# config.py
import os
# 调试模式
DEBUG = True
USE_EVALEX = False
# 获取项目目录
APP_PATH = os.path.dirname(__file__)
# sqlite数据库url
# SQLALCHEMY_DATABASE_URI = f'sqlite:///{APP_PATH}/db/health.db'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/health'
# 是否追踪数据的修改
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
# 是否显示生成sql语句
SQLALCHEMY_ECHO = False

# APSCHEDULER_SCHEDULER_CLASS = 'flask_apscheduler.schedulers.BackgroundScheduler'

TIMEOUT = 1
# 其他配置...
# JOBS = [
#         {
#             'id': 'job1',
#             'func': 'web.tasks.update_status',
#             'trigger': 'cron',
#             'trigger': 'interval',
#             'seconds': 10
#         }
#     ]
SCHEDULER_API_ENABLED = True
SCHEDULER_TIMEZONE = 'Asia/Shanghai'
