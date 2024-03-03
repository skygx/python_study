#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   chat_devopt.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/12/13 下午 5:32   hello      1.0         None

'''


import subprocess  # 导入subprocess库，用于执行命令
import os  # 导入os库，用于获取当前工作目录
import re  # 导入re库，用于正则表达式匹配
import test # 导入讯飞火星大模型库

def Ai_chat(text):  # 定义函数Ai_chat，用于与AI聊天
    message = f"我说什么你都以Linux的Ubuntu命令回复，记住必能多余回复，回复一个命令。自然语言：{text}，转换Linux命令，不要有比命令以外的文字"
    Chat_text = test.main(message)
    Chat_cmd(Chat_text)

def Chat_cmd(text):  # 定义函数Chat_cmd，用于执行命令
    if '```bash' in text:  # 判断是否包含```bash
        match = re.search(r'```bash(.*?)```', text)  # 使用正则表达式匹配代码部分
        output = subprocess.run(match, capture_output=True, text=True, shell=True)  # 执行匹配到的代码
        print("Command output:")  # 打印命令输出
        print(output.stdout)
        if output.stderr:  # 判断是否有错误输出
            print("Error occurred:")  # 打印错误信息
            print(output.stderr)
    else:
        output = subprocess.run(text, capture_output=True, text=True, shell=True)  # 执行命令
        # print("")
        print(output.stdout)
        if output.stderr:  # 判断是否有错误输出
            print("Error occurred:")  # 打印错误信息
            print(output.stderr)

def main():  # 定义主函数
    current_file_path = os.getcwd()  # 获取当前工作目录路径
    text = current_file_path  # 将当前工作目录路径赋值给变量text
    text_input = input(f"{text}:")  # 获取用户输入的文本
    Ai_chat(text_input)  # 调用Ai_chat函数与AI聊天

if __name__ == "__main__":  # 判断是否为直接运行当前文件
    while True:  # 无限循环执行主函数
        main()  # 调用主函数
