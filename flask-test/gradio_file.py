#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   gradio_file.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/29 下午 2:43   hello      1.0         None

'''
import gradio as gr
import pandas as pd


def read_excel_and_show(file_path):
    print(file_path)
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        return df
    except FileNotFoundError:
        print("文件未找到，请检查文件路径是否正确。")
    except Exception as e:
        print(f"读取文件时发生错误：{e}")

# 创建一个gradio界面，包含一个输入组件用于上传文件和一个展示DataFrame的组件
gr.Interface(
    fn=read_excel_and_show,
    inputs="file",
    outputs="dataframe"
).launch(server_name='0.0.0.0', server_port=8080, show_error=True,share=True)

# if __name__ == '__main__':
#     df = read_excel_and_show(r"D:\project\Pyproject\python_study\flask-test\test.xlsx")
#     print(df)
