# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   gradio_url.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/12/4 上午10:20   hello      1.0         None

'''
import gradio as gr

def greet():
    return f"Hello!"

interface = gr.Interface(fn=greet, inputs="text", outputs="text")
interface.launch(share=True)
