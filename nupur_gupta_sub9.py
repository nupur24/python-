# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:35:27 2018

@author: HP
"""

a= raw_input("enter numbers :" ).split(",")
#print a
a = [int(i) for i in a]
#print a
a.sort()
a.pop()
a.pop(0)
print sum(a)/len(a)


