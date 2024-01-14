#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   generate_redis_datas.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/11/29 上午 10:39   hello      1.0         None

'''

import random
import string
from faker import Faker
from datetime import datetime
fake = Faker(locale='zh_CN')

def random_string(len):
    return ''.join(random.sample(string.ascii_letters + string.digits, len))

def createDataFile(fileName):

    f = open(fileName, "w")

    # sample data

    # data = ["ABC", "DEFG", "HIJKL", "MNOPQR", "STUVWXYZ"]

    # random_str = random_string(5)
    # print(random_str)
    # rastr=fake.pystr(min_chars=3, max_chars=8)
    # di=fake.pydict(nb_elements=10, variable_nb_elements=True)
    # print(rastr)
    # print(di)
    # print(fake.ssn(min_age=18, max_age=90))

    # randomly generate 100 lines of data

    for i in range(100):

        # new_word = random.choice(data) + str(random.randint(1, 100))
        new_word = fake.pystr(min_chars=3, max_chars=8) + str(random.randint(1, 100))
        f.write(new_word + "\n")

    f.close()
    print("create Data File done!")

createDataFile("sampleData.txt")
