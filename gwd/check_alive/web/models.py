# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   models.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/24 下午3:19   hello      1.0         None

'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, scoped_session

import os

app = Flask(__name__)
# 【1】注释以下两行后可能会报错： RuntimeError: Either 'SQLALCHEMY_DATABASE_URI' or 'SQLALCHEMY_BINDS' must be set.
app_ctx = app.app_context()
app_ctx.push()
app.config.from_object('config')
# app.config.from_object(BaseConfig)
# app.secret_key = 'dev'
# 创建数据库连接，管理项目
db = SQLAlchemy(app, session_options={"autoflush": False, "autocommit": False})

# class BaseConfig():
#     DEBUG = True
#     # 获取项目目录
#     APP_PATH = os.path.dirname(__file__)
#     # sqlite数据库url
#     # SQLALCHEMY_DATABASE_URI = f'sqlite:///{APP_PATH}/db/health.db'
#     SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/health'
#     # 是否追踪数据的修改
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#     SQLALCHEMY_COMMIT_ON_TEARDOWN = True
#     # 是否显示生成sql语句
#     SQLALCHEMY_ECHO = False

# engine = db.engine(pool_size=50, max_overflow=0, pool_timeout=30, pool_recycle=1800)
# Session = scoped_session(sessionmaker(bind=engine))
# Session = sessionmaker(bind=engine)

class Url(db.Model):  # 模型类继承db.Model
    __tablename__ = 'url'
    """创建User表"""
    #  SQLAlchemy 需要手动执行主键列，第一个参数是 字段类型，第二个参数是约束条件
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    env = db.Column(db.String(20))
    name = db.Column(db.String(20))
    ip = db.Column(db.String(20))
    port = db.Column(db.String(6))
    location = db.Column(db.String(10))
    url = db.Column(db.String(40))
    key = db.Column(db.String(20))
    status = db.Column(db.String(10),nullable=True)
    # 【2】若想增加一个字段，run之后并没有加入表中，可以先删除表，再run,然后刷新即可加入（因为该表已存在，不会重新创建表了）
    desc = db.Column(db.String(40),nullable=True)

    # def __enter__(self):
    #     db.session.begin_nested()
    #     return self

    # def __exit__(self):
    #     db.session.close()
    #     db.session.remove()

    # def __repr__(self):
    #     return f'<Url {self.env} {self.name} {self.ip} {self.port} {self.location} {self.url} {self.key} {self.status} {self.desc}>'

    def is_status_null(self):
        status = Url.query.filter_by(status=None).all()
        return status

    def create_item(self, env, name, ip, port, location, url, key,status=None,desc=None):
        self.env = env
        self.name = name
        self.ip = ip
        self.port = port
        self.location = location
        self.url = url
        self.key = key
        self.status = status
        self.desc = desc
        print(f'{env} {name} {ip} {port} {location} {url} {key} {status} {desc}')
        try:
            db.session.add(self)
            db.session.commit()
            print(f'添加成功')
        except Exception as e:
            print(f'添加失败：{e}')
            db.session.rollback()
        finally:
            db.session.close()
            # db.session.remove()
    def read_item_by_id(self, id):
        item = Url.query.get(id)
        return item

    def read_item_by_ids(self, ids):
        ids = ids.replace('[', '').replace(']', '').split(',')
        ids = [str(id) for id in ids]
        # print(ids)
        items = Url.query.filter(Url.id.in_(ids)).all()
        return items
    def read_item_by_env(self, env):
        items = Url.query.filter_by(env=env).all()
        return items

    def read_all_item(self):
        items = Url.query.all()
        return items

    def alter_id(self):
        try:
            db.session.begin()
            db.session.execute(db.text("alter table url drop column id"))
            db.session.execute(db.text("alter table url add column id INT PRIMARY KEY AUTO_INCREMENT"))
            db.session.commit()
            print('id字段修改成功')
        except Exception as e:
            print(f'id字段删除失败：{e}')
            db.session.rollback()
        finally:
            db.session.close()
            # db.session.remove()
    def update_status_by_id(self, id, status):
        item = Url.query.filter_by(id=id)
        item.status = status
        try:
            db.session.commit()
            print(f'Item {id} status updated')
        except Exception as e:
            print(f'更新失败：{e}')
            db.session.rollback()
        finally:
            db.session.close()
            # db.session.remove()
    def update_item(self, id, data):
        item = Url.query.get(id)
        item.name = data.get('name')
        item.ip = data.get('ip')
        item.port = data.get('port')
        item.env = data.get('env')
        item.location = data.get('location')
        item.url = data.get('url')
        item.key = data.get('key')
        item.status = data.get('status')
        item.desc = data.get('desc')
        try:
            db.session.commit()
            print(f'Item {id} updated')
        except Exception as e:
            print(f'更新失败：{e}')
            db.session.rollback()
        finally:
            db.session.close()
            # db.session.remove()
        # self.alter_id()

    def delete_item(self, id):
        item = Url.query.filter_by(id=id).first()
        if item:
            try:
                db.session.delete(item)
                db.session.commit()
            except Exception as e:
                print(f'删除失败：{e}')
                db.session.rollback()
            finally:
                db.session.close()
                # db.session.remove()
            print(f'Item {id} deleted')
        else:
            print(f'Item {id} not found')
        self.alter_id()

    def delete_items_by_ids (self, ids):
        ids = ids.replace('[', '').replace(']', '').split(',')
        ids = [str(id) for id in ids]
        items = Url.query.filter(Url.id.in_(ids)).all()
        for item in items:
            try:
                db.session.delete(item)
                db.session.commit()

            except Exception as e:
                print(f'删除失败：{e}')
                db.session.rollback()
            finally:
                db.session.close()
                # db.session.remove()
        print(f'Items {ids} deleted')
        self.alter_id()

    def delete_all_item(self):
        try:
            db.session.query(Url).delete()
            db.session.commit()
            print('All items deleted')
        except Exception as e:
            print(f'删除失败：{e}')
            db.session.rollback()
        finally:
            db.session.close()
            # db.session.remove()

def bulk_insert(data):
    try:
        db.session.bulk_insert_mappings(Url, data).on_duplicate_key_ignore()
        db.session.commit()
        print(f'批量添加成功')

    except Exception as e:
        print(f'批量添加失败：{e}')
        db.session.rollback()
    finally:
        db.session.close()
        # db.session.remove()

if __name__ == '__main__':
    # 【3】删除所有表，注意这条是危险命令，会将模型类对应数据库中的表物理删除。在实际生产环境下勿用。
    # db.drop_all()
    # db.create_all()  # 创建所有的表

    # 创建测试数据
    # url = Url()
    # url.create_item('ver', 'nginx', '192.168.226.20', '80', 'mp', 'index.html', 'nginx'  )
    # url = Url()
    # url.create_item('ver', 'backup', '192.168.226.20', '88', 'mp', 'bk_svr', 'hello'   )
    # url = Url()
    # url.create_item('prod', 'ip', '192.168.226.20', '88', 'pbs', 'ip', 'hello'  )
    # url = Url()
    # url.create_item('prod', 'info', '192.168.226.20', '80', 'pbs', 'log.html', 'info'  )
    # url = Url()
    # url.create_item('prod', 'bk1', '192.168.226.20', '88', 'mp', 'bk_svr1', 'hello'  )


    data = [
        {'env': 'ver', 'name': 'nginx', 'ip': '192.168.226.20', 'port': '80', 'location': 'mp', 'url': 'index.html', 'key': 'nginx', 'status': '','desc':''},
        {'env': 'ver', 'name': 'backup', 'ip': '192.168.226.20', 'port': '88', 'location': 'mp', 'url': 'bk_svr', 'key': 'hello', 'status': '','desc':''},
        {'env': 'prod', 'name': 'ip', 'ip': '192.168.226.20', 'port': '88', 'location': 'pbs', 'url': 'ip', 'key': 'hello', 'status': '','desc':''},
        {'env': 'prod', 'name': 'info', 'ip': '192.168.226.20', 'port': '80', 'location': 'pbs', 'url': 'log.html', 'key': 'info', 'status': '','desc':''},
        {'env': 'prod', 'name': 'bk1', 'ip': '192.168.226.20', 'port': '88', 'location': 'mp', 'url': 'bk_svr1', 'key': 'hello', 'status': '','desc':''},
        {'env': 'prod', 'name': 'acct', 'ip': '192.168.226.20', 'port': '80', 'location': 'mp', 'url': 'health', 'key': 'body', 'status': '','desc':''},
        {'env': 'prod', 'name': 'loan', 'ip': '192.168.226.20', 'port': '88', 'location': 'mp', 'url': 'gateway', 'key': 'hello', 'status': '','desc':''},
        {'env': 'prod', 'name': 'limt', 'ip': '192.168.226.20', 'port': '88', 'location': 'mp', 'url': 'least', 'key': 'hello', 'status': '','desc':''},
        {'env': 'ver', 'name': 'bank', 'ip': '192.168.226.20', 'port': '88', 'location': 'mp', 'url': 'url', 'key': 'hello', 'status': '','desc':''},
        {'env': 'ver', 'name': 'fcs', 'ip': '192.168.226.20', 'port': '80', 'location': 'mp', 'url': 'status', 'key': 'server', 'status': '','desc':''},
        {'env': 'uat', 'name': 'ecmn', 'ip': '192.168.226.20', 'port': '88', 'location': 'mp', 'url': 'gateway1', 'key': 'hello', 'status': '','desc':''},
        {'env': 'fat', 'name': 'cup', 'ip': '192.168.226.20', 'port': '88', 'location': 'mp', 'url': 't1', 'key': 'html', 'status': '','desc':''},
        {'env': 'pet', 'name': 'unit', 'ip': '192.168.226.20', 'port': '88', 'location': 'mp', 'url': 'api', 'key': '1', 'status': '','desc':''},
        {'env': 'prod', 'name': 'fcs', 'ip': '192.168.226.20', 'port': '88', 'location': 'mp', 'url': 'api/bk_svr', 'key': 'hello', 'status': '','desc':''},
        {'env': 'prod', 'name': 'fcs', 'ip': '192.168.226.20', 'port': '80', 'location': 'mp', 'url': 'nginx_status', 'key': 'server', 'status': '','desc':''},
        {'env': 'prod', 'name': 'fcs', 'ip': '192.168.226.20', 'port': '80', 'location': 'mp', 'url': 'tomcat', 'key': 'tomcat', 'status': '','desc':''}
    ]
    bulk_insert(data)
    # url = Url()
    # url.alter_id()

    # 查詢所有数据指定env
    # url=Url()
    # items = url.read_item_by_env('ver')
    # print(url.is_status_null())

    # 删除指定id的数据
    # url=Url()
    # url.delete_items_by_ids([1,3,4])

    # 插入数据
    # url1=Url('ver', 'nginx', '192.168.226.20', '80', 'mp', 'index.html', 'nginx','' )
    # url2=Url('ver', 'backup', '192.168.226.20', '88', 'mp', 'bk_svr', 'hello' ,'')
    # url3=Url('prod', 'ip', '192.168.226.20', '88', 'pbs', 'ip', 'hello' ,'' )
    # url4=Url('prod', 'info', '192.168.226.20', '80', 'pbs', 'log.html', 'info',''  )
    # url5=Url('prod', 'bk1', '192.168.226.20', '88', 'mp', 'bk_svr1', 'hello','' )
    # db.session.add_all([url1,url2,url3,url4,url5])

    # 读取数据
    # item = url.read_item(1)
    # item = url.read_all_item()
    # print(item)
    pass
