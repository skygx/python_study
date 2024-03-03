#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   diff_text.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/22 下午 3:45   hello      1.0         None

'''
import difflib
import click

# @click.command()
# @click.option("-t","--text", prompt='Please input output format: ',
#               help='output format')
def main():
    text1 = '''text1:
    This module provides classes and functions for comparing sequences.
    including HTML and context and unified diffs
    difflib document v7.4
    add string    
    '''
    text1_lines = text1.splitlines()
    text2 = '''text2:
    This module provides classes and functions for Comparing sequences.
    including HTML and context and unified diffs
    difflib document v7.5'''
    text2_lines = text2.splitlines()

    # d = difflib.Differ()
    # diff = d.compare(text1_lines,text2_lines)
    # print('\n'.join(list(diff)))

    d = difflib.HtmlDiff()
    print(d.make_file(text1_lines,text2_lines))

if __name__ == '__main__':
    main()
