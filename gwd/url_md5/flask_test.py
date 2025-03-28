# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   flask_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/12/4 上午10:30   hello      1.0         None

'''
import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
