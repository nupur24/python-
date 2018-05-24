# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:02:03 2018

@author: HP
"""

a= raw_input("enter string:")
print a
dict1 = {}
 
for i in a:
    b=a.count(i)
    dict1[i]=b

print dict1
     