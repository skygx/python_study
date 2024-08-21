#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   diff_file_report_1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/4/4 上午 10:39   hello      1.0         None

'''
import sys

import difflib

import time

import os

"""

创作时间：2017-10-08 23:30 09

版本： 1.0.0

"""

def main():

    """主函数"""
    try:

        f1 = sys.argv[1]  # 获取文件名

        f2 = sys.argv[2]

    except Exception as e:

        print("Error: " + str(e))

        print("Usage : python diff_file_report_1.py filename1 filename2")

        sys.exit()

    if f1 == "" or f2 == "":  # 参数不够

        print("Usage : python diff_file_report_1.py filename1 filename2")

        sys.exit()

    tf1 = readFile(f1)

    tf2 = readFile(f2)

    d = difflib.HtmlDiff()  # 创建一个实例difflib.HtmlDiff

    writeFile(d.make_file(tf1, tf2))  # 生成一个比较后的报告文件，格式为html


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

    diffFile.write("")

    diffFile.write(file)

    print("The file on {}".format(os.path.abspath(str(diffFile.name))))  # 提示文件生成在什么地方

    diffFile.close()

if __name__ == "__main__":

    main()
