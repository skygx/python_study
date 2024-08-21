# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   batch_insert_sqlite.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/26 下午2:43   hello      1.0         None

'''

import sqlite3

conn = sqlite3.connect('db/health.db')
cursor = conn.cursor()

# 开始事务
cursor.execute('BEGIN')

# 插入数据
# cursor.execute('INSERT INTO url VALUES (?, ?,?,?,?,?,?,?,?)', ('uat','acct','192.168.226.20','80','mp','ret','xin','',''))
# cursor.execute('INSERT INTO url VALUES (?, ?,?,?,?,?,?,?,?)', ('fat','loan','192.168.226.20','80','mp','status','server','',''))
# cursor.execute('INSERT INTO url VALUES (?, ?,?,?,?,?,?,?,?)', ('pet','loan','192.168.226.20','80','pbs','test','txt','',''))

data = [
('uat','acct','192.168.226.20','80','mp','ret','xin'),
('fat','loan','192.168.226.20','80','mp','status','server'),
('pet','loan','192.168.226.20','80','pbs','test','txt')
]
cursor.executemany('INSERT INTO url(env,name,ip,port,env,url,key) VALUES (?,?,?,?,?,?,?)', data)
# 提交事务
cursor.execute('COMMIT')

conn.close()
