# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:11:07 2018

@author: HP
"""

a= raw_input("enter numbers :" ).split(",")
print a

a = [int(i) for i in a]
flag=0

a = [10, 3, 4, 1, 13, 13, 4]


ind = 0

while 13 in a:
    ind = a.index(13)
    a.remove(13)
    if ind < (len(a)-1):
        temp = a[ind+1]
        a.remove(temp)
    
print sum(a)
    
    
    
    






