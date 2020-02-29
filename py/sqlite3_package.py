#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:sqlite3_package.py
    功能:
    版本:1.0
    日期:2019/2/18 10:01
'''

import sqlite3


def create_table(conn):
    c = conn.cursor()

    c.execute('''CREATE TABLE category
                (id int primary key, 
                 sort int, 
                 name text)''')

    c.execute('''CREATE TABLE book
                (id int primary key,
                 sort int,
                 name text,
                 price real,
                 category int,
                 FOREIGN KEY (category) REFERENCES category(id))''')

    conn.commit()


def insert_table(conn):
    c = conn.cursor()

    books = [(1, 1, 'Cook Recipe', 3.12, 1),
             (2, 3, 'Python Intro', 17.5, 2),
             (3, 2, 'OS Intro', 13.6, 2),
             ]

    # execute "INSERT"
    c.execute("INSERT INTO category VALUES (1, 1, 'kitchen')")

    # using the placeholder
    c.execute("INSERT INTO category VALUES (?, ?, ?)", [2, 2, 'computer'])

    # execute multiple commands
    c.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)

    conn.commit()


def query_table(conn):
    c = conn.cursor()

    # retrieve one record
    c.execute('SELECT name FROM category ORDER BY sort')
    print(c.fetchone())
    print(c.fetchone())

    # retrieve all records as a list
    c.execute('SELECT * FROM book WHERE book.category=1')
    print(c.fetchall())

    # iterate through the records
    for row in c.execute('SELECT name, price FROM book ORDER BY sort'):
        print(row)


def update_table(conn):
    c = conn.cursor()

    c.execute('UPDATE book SET price=? WHERE id=?', (1000, 1))
    c.execute('DELETE FROM book WHERE id=2')

    conn.commit()


def delete_table(conn):
    c = conn.cursor()
    c.execute('DELETE FROM book')
    books = [(1, 1, 'Cook Recipe', 3.12, 1),
             (2, 3, 'Python Intro', 17.5, 2),
             (3, 2, 'OS Intro', 13.6, 2),
             ]
    c.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)
    conn.commit()


def drop_table(conn):
    c = conn.cursor()
    c.execute('drop table category')
    conn.commit()


def main():
    conn = sqlite3.connect("test.db")
    # create_table(conn)
    insert_table(conn)
    # delete_table(conn)
    query_table(conn)
    # update_table(conn)
    print('*'*50)
    # query_table(conn)
    # drop_table(conn)
    conn.close()



if __name__ == '__main__':
    main()
