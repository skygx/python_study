#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   redis_cache.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/22 下午 2:16   hello      1.0         None

'''
from flask import Flask, jsonify
from flask_redis import FlaskRedis
import time


app = Flask(__name__)


# flask-redis 的配置和初始化
app.config['REDIS_URL'] = 'redis://:admin@192.168.226.20:6380/0'
redis_client = FlaskRedis(app)


@app.route('/')
def index():
    return 'Hello World'

@app.route('/set_data/<int:id>')
def set_data(id):
    # 准备相关的数据
    user_id = str(id)
    data = 'dyn_data_{}'.format(user_id)
    data_key = 'dyn_key_{}'.format(user_id)
    # 设置超时时间为 60 秒，当动态数据超过 60 没有更新时，Redis 会自动清除该数据。
    expires = int (time.time()) + 60

    # 写入 redis 中
    # 通过管道 pipeline 来操作 redis，以减少客户端与 redis-server 的交互次数。
    p = redis_client.pipeline()
    p.set(data_key, data)
    p.expireat(data_key, expires)
    p.execute()

    return '设置成功'

@app.route('/get_data/<int:id>')
def get_data(id):
    user_id = str(id)
    data_key = 'dyn_key_{}'.format(user_id)
    data = redis_client.get(data_key)

    print('data = {}'.format(data))

    if data:
        return jsonify(
            {
                'data': data.decode(),
            }
        )
    else:
        return jsonify({})

if __name__ == '__main__':
    # 运行Flask应用
    app.run(port=5000)
