#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python-note 
@File    ：number.py
@Author  ：fredz
@Date    ：2022/6/14 23:34 
"""
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)

print(2 ** 3)

print(0.1 + 0.1)
#
print(0.1 + 0.2)
print(0.1 + 0.4)

print(4 / 2)
print(1 + 0.1)
print(1 * 0.1)
print(3.0 ** 2)

universe_age = 12_000_000
print(universe_age)
# 存储带有下划线的数字时 会忽略下划线  适用于整数和浮点数

x, y, z = 1, 1, 1
# a, b = 1
print(x, y, z)
# print(a, b)

# Traceback (most recent call last):
#   File "/Users/fredz/code/python-note/variable&datatype/data_type/number.py", line 31, in <module>
#     a, b = 1
# TypeError: cannot unpack non-iterable int object
# 多个变量赋值 变量和值的个数保持相同
