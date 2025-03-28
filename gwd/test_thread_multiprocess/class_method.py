# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   class_method.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/26 下午1:46   hello      1.0         None

'''
class Student:
    school_name = "ABC School"  # 类属性

    def __init__(self, name, grade):
        self.name = name  # 实例属性
        self.grade = grade  # 实例属性

    # 普通方法
    def display_info(self):
        print(f"普通方法: {self.name} is in grade {self.grade} at {self.school_name}.")

    # 类方法
    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school
        print(f"类方法: School changed to {cls.school_name}")

    # 静态方法
    @staticmethod
    def is_passing_grade(grade):
        return grade >= 50

# 使用
# 创建实例
student1 = Student("Alice", 85)
student2 = Student("Bob", 45)

# 普通方法
student1.display_info()  # 输出: 普通方法: Alice is in grade 85 at ABC School.

# 类方法
Student.change_school("XYZ School")  # 输出: 类方法: School changed to XYZ School
student2.display_info()  # 输出: 普通方法: Bob is in grade 45 at XYZ School.

# 静态方法
print(f"静态方法: Is Alice passing? {Student.is_passing_grade(student1.grade)}")  # 输出: 静态方法: Is Alice passing? True
print(f"静态方法: Is Bob passing? {Student.is_passing_grade(student2.grade)}")  # 输出: 静态方法: Is Bob passing? False
