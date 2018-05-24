# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:02:54 2018

@author: HP
"""

lst = input("Enter: ")

check = 0
total = 0

for i in lst:
    if i == 13:
        check = 1
    if check == 0:
        total += i
    elif check == 1 and i != 13:
        check = 0

print total