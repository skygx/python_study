#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   gradio_temp.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/28 下午 5:43   hello      1.0         None

'''
import gradio as gr
#该函数有3个输入参数和2个输出参数
def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)
demo = gr.Interface(
    fn=greet,
    #按照处理程序设置输入组件
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    #按照处理程序设置输出组件
    outputs=["text", "number"],
)
demo.launch(server_name='0.0.0.0', server_port=8080, show_error=True)
