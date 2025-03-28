# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   class_property.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/26 上午10:54   hello      1.0         None

'''
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    def get_age(self):
        return self._age

    def set_age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a positive integer")
        self._age = value

    # 使用 property() 函数
    name = property(get_name, set_name)
    age = property(get_age, set_age)

# 测试
person = Person("Alice", 25)
print(f"Name: {person.name}")
print(f"Age: {person.age}")

person.name = "Bob"
person.age = 30
print(f"Updated Name: {person.name}")
print(f"Updated Age: {person.age}")
