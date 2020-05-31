#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   example-1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30  19:14   xguo      1.0         None

'''
import string


def translator(frm='', to='', delete='', keep=None):
    if len(to) == 1:
        to = to*len(frm)
    trans=string.maketrans(frm,to)
    if keep is not None:
        allchars=string.maketrans('', '')
        delete = allchars.translate(allchars, keep.translate(allchars, delete))
    def translate(s):
        return s.translate(trans, delete)
    return translate


def main():
    user_input = "This\nstring has\tsome whitespaces...\r\n"
    print(user_input)
    # character_map = {
    #     ord('\n'): ' ',
    #     ord('\t'): ' ',
    #     ord('\r'): None
    # }
    # intab = 'aeiou'
    # outtab = '12345'
    intab = '\n\t\r'
    outtab = '   '
    deltab = 'twh'

    trantab = str.maketrans(intab,outtab)

    # user_input.translate(character_map)  # This string has some whitespaces... "
    print(user_input.translate(trantab))


if __name__ == "__main__":
    main()