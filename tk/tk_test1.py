#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   tk_test1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/1/10 下午 12:36   hello      1.0         None

'''
import tkinter as tk

def show_input(event):
    print("Input is:", entry.get())

root = tk.Tk()
entry = tk.Entry(root)
entry.bind("<Return>", show_input)
entry.pack()

root.mainloop()
