#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:records-test.py
    功能:用records标准库访问mysql数据库和操作
    版本:1.0
    日期:2019/12/214:19
'''
import records

def main():
    db=records.Database('mysql+pymysql://root:root@localhost:3306/test')
    select_sql='''select * from test1'''
    db.query("insert into test1 values('1','li')")
    users=[
        {'name':'hu','id':6},
        {'name':'lin','id':7},
        {'name':'zhang','id':8}
    ]
    db.bulk_query("insert into test1 values (:id,:name)",users)
    rows=db.query(select_sql)
    with open('test1_db.csv','wb') as f:
        f.write(rows.export('xls'))
    print(rows.all())


if __name__ == "__main__":
    main()