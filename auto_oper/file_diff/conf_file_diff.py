#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   conf_file_diff.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/22 下午 4:01   hello      1.0         None

'''
import difflib
import sys

def main():
    try:
        textfile1 = sys.argv[1]
        textfile2 = sys.argv[2]
    except Exception as e:
        print("Error:"+str(e))
        print("Usage: conf_file_diff.py filename1 filename2")
        sys.exit()
    if textfile1 == "" or textfile2 == "":
        print("Usage: conf_file_diff.py filename1 filename2")
        sys.exit()
    text1_lines = readfile(textfile1)
    text2_lines = readfile(textfile2)
    d = difflib.HtmlDiff()
    print(d.make_file(text1_lines,text2_lines))

def readfile(filename):
    try:
        fileHandle = open(filename, 'rb')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print('Read file Error:'+str(error))
        sys.exit()

if __name__ == '__main__':
    main()
