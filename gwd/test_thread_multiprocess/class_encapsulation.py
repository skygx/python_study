# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   class_encapsulation.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/26 上午10:53   hello      1.0         None

'''
class Person:
    def __init__(self, name, age):
        self._name = name  # 使用 _ 表示私有属性
        self._age = age

    @property
    def name(self):
        """Getter for name"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name"""
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def age(self):
        """Getter for age"""
        return self._age

    @age.setter
    def age(self, value):
        """Setter for age"""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a positive integer")
        self._age = value

# 测试
person = Person("Alice", 25)

# 访问属性（调用 getter）
print(f"Name: {person.name}")
print(f"Age: {person.age}")

# 修改属性（调用 setter）
person.name = "Bob"
person.age = 30

print(f"Updated Name: {person.name}")
print(f"Updated Age: {person.age}")

# 测试异常
try:
    person.age = -5  # 非法值
except ValueError as e:
    print(e)

try:
    person.name = ""  # 非法值
except ValueError as e:
    print(e)
