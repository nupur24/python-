# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:26:47 2018

@author: HP
"""

a= raw_input("enter sting:")
print a
d=0
l=0

for i in a:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
        
print ("l=",l)
print ("d=",d)        
    
    




