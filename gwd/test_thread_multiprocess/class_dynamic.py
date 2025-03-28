# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   class_dynamic.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/26 下午1:58   hello      1.0         None

'''

from math import pi

class Shape:
    def area(self):
        raise NotImplementedError("子类必须实现此方法")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def update_radius(self, new_radius):
        self.radius = new_radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def update_dimensions(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

# 动态修改属性值并计算面积
def calculate_and_update(shape):
    print(f"初始面积: {shape.area()}")

    # 动态修改属性值
    if isinstance(shape, Circle):
        shape.update_radius(5)  # 修改圆的半径
    elif isinstance(shape, Rectangle):
        shape.update_dimensions(4, 6)  # 修改矩形的宽高

    # 重新计算面积
    print(f"修改属性值后的面积: {shape.area()}")

# 测试
circle = Circle(3)
rectangle = Rectangle(2, 3)

# 使用多态性处理不同的形状
shapes = [circle, rectangle]
for shape in shapes:
    calculate_and_update(shape)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# 动态修改属性值
def update_shape(shape, **kwargs):
    for key, value in kwargs.items():
        setattr(shape, key, value)
    print(f"更新后的面积: {shape.area()}")

# 测试
triangle = Triangle(3, 4)
print(f"初始面积: {triangle.area()}")

# 动态修改属性
update_shape(triangle, base=8, height=10)
