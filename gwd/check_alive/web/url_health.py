# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   url_health.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/24 下午5:21   hello      1.0         None

'''

from flask import request, jsonify, render_template, send_file
from flask_cors import CORS
import pandas as pd
from logics import *


# 设置内存限制为100MB
# MAX_MEMORY = 100000000
#
# @app.before_request
# def check_memory_usage():
#     snapshot = tracemalloc.take_snapshot()
#     _, peak = snapshot.statistics('lineno')[-1]
#
#     if peak > MAX_MEMORY:
#         abort(413, 'Request entity too large')

CORS(app)
# app_ctx = app.app_context()
# app_ctx.push()


def app_env(env):
    data = get_url_status_from_env(env)
    # print(data)
    return jsonify(data)


def excel_export():
    ids = request.args.get('ids')
    data = export_data(ids)
    df = pd.DataFrame(data)
    df.to_excel('output.xlsx', index=False)
    return send_file('output.xlsx', as_attachment=True)


def all():
    data = get_all_message()
    # print(data)
    # response = make_response(jsonify(data))
    # response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    # response.headers["Pragma"] = "no-cache"
    # response.headers["Expires"] = "0"
    return jsonify(data)


def index():
    return render_template('all.html', title='Home')


def form():
    if request.method == 'POST':
        insert_data_to_db(request.form)
        # clear_cache()
        return render_template('all.html',title='All Message')
    else:
        return render_template('form.html', title='Form')


def pages(env):
    return render_template('page.html', title=env, env=env)


def all_message():
    return render_template('all.html', title='All Message')


def delete_urls():
    ids = request.args.get('ids')
    url = Url()
    url.delete_items_by_ids(ids)
    return render_template('all.html', title='All Message')


def view_url(id):
    data = get_item_message_by_id(id)
    return jsonify(data)


def edit_url(id):
    if request.method == 'GET':
        data = get_item_message_by_id(id)
        return jsonify(data)
    else:
        print(request.form)
        data = request.form
        url = Url()
        url.update_item(id,data=data)
        return render_template('all.html', title='All Message')

# 老版本  读取ver1.txt文件获取数据
def health():
    data=get_url_list('url/ver1.txt')
    print(data)
    return jsonify(data)

# 老版本  直向ver1.html页面
def ver1():
    return render_template('ver1.html', title='VER1')

# 老版本 删除一个id的url
def delete_url():
    id = request.args.get('id')
    url = Url()
    url.delete_items_by_ids(id)
    return render_template('all.html', title='All Message')

# @app.teardown_appcontext
# def teardown_appcontext(exception):
#     # 在程序关闭前移除所有任务，并关闭调度器
#     if scheduler.running:
#         scheduler.remove_all_jobs()
#         scheduler.shutdown()

if __name__ == '__main__':
    app.add_url_rule('/api/<env>', view_func=app_env, methods=['GET'])
    app.add_url_rule('/api/view/<id>', view_func=view_url, methods=['GET'])
    app.add_url_rule('/api/edit/<id>', view_func=edit_url, methods=['GET','POST'])
    app.add_url_rule('/api/export', view_func=excel_export, methods=['GET'])
    app.add_url_rule('/api/all', view_func=all, methods=['GET'])
    app.add_url_rule('/api/form', view_func=form, methods=['GET', 'POST'])
    app.add_url_rule('/<env>/', view_func=pages, methods=['GET'])
    app.add_url_rule('/all/', view_func=all_message, methods=['GET'])
    app.add_url_rule('/api/delete', view_func=delete_urls, methods=['GET','POST'])
    app.add_url_rule('/', view_func=index, methods=['GET'])

    app.add_url_rule('/health', view_func=health, methods=['GET'])
    app.add_url_rule('/ver1', view_func=ver1, methods=['GET'])
    app.add_url_rule('/operator/delete', view_func=delete_url, methods=['GET'])
    # tracemalloc.start()

    scheduler.start()
    app.run(debug=True, host='0.0.0.0', port=5000)
    # scheduler.shutdown()
