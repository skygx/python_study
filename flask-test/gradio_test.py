#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   gradio_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/28 下午 5:10   hello      1.0         None

'''
import gradio as gr
#输入文本处理程序
def greet(name):
    return "Hello " + name + "!"
#接口创建函数
#fn设置处理函数，inputs设置输入接口组件，outputs设置输出接口组件
#fn,inputs,outputs都是必填函数
demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch(server_name='0.0.0.0', server_port=8080, show_error=True)
