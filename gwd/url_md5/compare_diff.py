# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   compare_diff.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/11/27 下午12:15   hello      1.0         None

'''
import re
import json
def compare_diff(data1,data2):
    d1=data1.split('\n')
    d2=data2.split('\n')
    df1 = {}
    df2 = {}
    diff = {}

    for i in range(len(d1)):
        if d1[i] == '':
            continue
        md5 = re.split(r'\s+', d1[i])[0]
        app = re.split(r'\s+', d1[i])[1]
        df1[app] = md5

    # print(df1)
    for i in range(len(d2)):
        if d2[i] == '':
            continue
        md5 = re.split(r'\s+', d2[i])[0]
        app = re.split(r'\s+', d2[i])[1]
        df2[app] = md5

    # print(df2)
    for key in df1:
        if key in df2:
            if df1[key] != df2[key]:
                diff[key] = [df1[key],df2[key],'diff']
            else:
                diff[key] = [df1[key],df2[key],'equal']
        else:
            diff[key] = [df1[key],'','new']

    for key in df2:
        if key not in df1:
            diff[key] = ['',df2[key],'del']

    return diff


def main():
    with open('data1.txt','r') as f1:
        data1 = f1.read()

    with open('data2.txt','r') as f2:
        data2 = f2.read()

    diff = compare_diff(data1,data2)
    print(diff)

    with open('diff.txt','w') as f:
        for key,value in diff.items():
            f.write("{:<30} {:<32} {:<32} {:5} \n".format(key,value[0],value[1],value[2]))
        # json.dump(diff,f)

if __name__ == '__main__':
    main()
