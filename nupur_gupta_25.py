# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:48:00 2018

@author: HP
"""



l =[]

while True:
    str1=raw_input("enter : ")
    if not str1:
        break
    t=str1.split(',')
    l.append((t[0], int(t[1]), int(t[2])))
l.sort()    
print l    
    

















