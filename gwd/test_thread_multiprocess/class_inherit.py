# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   class_inherit.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/26 上午10:55   hello      1.0         None

'''
class Animal:  # 父类
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("子类必须实现此方法")

class Dog(Animal):  # 子类
    def speak(self):
        return f"{self.name} 说: 汪汪!"

class Cat(Animal):  # 子类
    def speak(self):
        return f"{self.name} 说: 喵喵!"

# 测试
dog = Dog("旺财")
cat = Cat("咪咪")
print(dog.speak())
print(cat.speak())

def animal_speak(animal):
    print(animal.speak())

animal_speak(dog)
animal_speak(cat)

