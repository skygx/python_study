#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:pymysql-test.py
    功能:利用递归绘制分形树
    版本:1.0
    日期:2019/12/214:12
'''
import pymysql

def main():
    conn=pymysql.connect(host='localhost',port=3306,user='root',password='root',charset='utf8mb4',database='test')
    cursor=conn.cursor()
    result=cursor.execute('select * from test1')
    # result=cursor.execute()
    print(result)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()