#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python-note 
@File    ：string.py
@Author  ：fredz
@Date    ：2022/6/14 22:41 
"""
"hi,Google"
'hi,Google'
'I told my friend,"Taylor is pretty!"'
"God bless you,'little boy'"

"'hello'"
print("'hello'")

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
# f字符串 f是format(设置格式)的简写
print(f"Hello, {full_name.title()}!")
full_name = "{} {}".format(first_name, last_name)
print(full_name)
print("Python")
print("\tPython")
print("Java\tPython\tC++")
print("Java\nPython\nC++")
print("Language:\n\tJava\n\tPython\n\tC++")

username = 'python'
password = ' python '
print(username)
print(password)
print(username == password)
print(password.lstrip() == username)
print(password.rstrip() == username)
print(password.strip() == username)
msg = "I'm a python student"
print(msg)

