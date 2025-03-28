# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   remove_space.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/12/3 下午3:08   hello      1.0         None

'''

def main():
    with open("date.yml", 'r') as f:
        text = f.read()
        # print(text)
        clean_text = text.replace(u"聽", " ")
    with open("date_clean.yml", 'w') as f:
        f.write(clean_text)

if __name__ == '__main__':
    main()
