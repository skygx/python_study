# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   test_gui-2.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/1/24 上午9:35   hello      1.0         None

'''
from nicegui import ui

def calculate():
    num1 = float(ui.input.value)
    num2 = float(ui.input.value)
    operation = ui.select.value
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        result = 'Invalid operation'
    ui.label(f'Result: {result}')

ui.label('Number 1:')
ui.input_number1 = ui.input()
ui.label('Number 2:')
ui.input_number2 = ui.input()

ui.label('Operation:')
ui.select = ui.select(options=['add', 'subtract', 'multiply', 'divide'])
ui.button('Calculate', on_click=calculate)
ui.run()
