#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python-note 
@File    ：variable.py
@Author  ：fredz
@Date    ：2022/6/14 22:27 
"""
message = "Hello, Python"
print(message)
# message即为变量 每个变量都指向一个值 message的值为 'Hello, Python'

message = "Hello, Google"
print(message)
# /usr/local/bin/python3.10 /Users/fredz/code/python-note/variable&datatype/variable/variable.py
# Hello, Python
# Hello, Google
# 说明程序中可以随时修改便令的值 python始终会记录变量的最新值

message_1 = "Hello"
_message = "Hello"
# 1_message = "Hello"
print(message_1)
# print(1_message)
#   File "/Users/fredz/code/python-note/variable&datatype/variable/variable.py", line 21
#     1_message = "Hello"
#      ^
# SyntaxError: invalid decimal literal
# 变量名能以字母或者下划线开头 但不能以数字开头

get_message = "Python"
# get message = "Python"
print(get_message)
# print(get message)
#   File "/Users/fredz/code/python-note/variable&datatype/variable/variable.py", line 32
#     get message = "Python"
#         ^^^^^^^
# SyntaxError: invalid syntax


# 不要使用python保留用作特殊用途的单词 eg:print

# 概念: 变量是标签 变量是可以赋值的标签 变量指向特定的值
