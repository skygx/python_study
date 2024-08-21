#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   diff_file_report_1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/4/4 上午 10:39   hello      1.1         None

'''
import sys

import difflib

import time

import os

def main():

    """主函数"""
    path = os.getcwd()
    traverse_folder(path)
    file1="db.properties"
    file2="db1.properties"
    report_html(file1,file2)

def traverse_folder(path):
    current_path=path
    for foldername, subfolders, filenames in os.walk(path):
        print('当前文件夹: ' + foldername)
        for subfolder in subfolders:
            print('- 子文件夹: ' + subfolder)
            # 改变当前工作目录
            os.chdir(subfolder)
            print(f"改变工作目录到: {os.getcwd()}")
            os.chdir(current_path)
        for filename in filenames:
            print('- 文件: ' + filename)
        print()


def report_html(filename1,filename2):

    if filename1 == "" or filename2 == "":  # 参数不够

        print("filename1 filename2 must be exist.")

        sys.exit()

    tf1 = readFile(filename1)

    tf2 = readFile(filename2)

    d = difflib.HtmlDiff()  # 创建一个实例difflib.HtmlDiff

    writeFile(d.make_file(tf1,tf2))  # 生成一个比较后的报告文件，格式为html


def readFile(filename):


    """读取文件，并处理"""

    try:

        fileHandle = open(filename, "r")

        text = fileHandle.read().splitlines()

        fileHandle.close()

        return text

    except IOError as e:

        print("Read file error: " + str(e))

        sys.exit()


def writeFile(file):


    """写入文件"""

    diffFile = open('diff_{}_.html'.format(time.strftime("%Y%m%d_%H%M%S", time.localtime())), "w")

    diffFile.write(file)

    print("The file on {}".format(os.path.abspath(str(diffFile.name))))  # 提示文件生成在什么地方

    diffFile.close()

if __name__ == "__main__":

    main()
