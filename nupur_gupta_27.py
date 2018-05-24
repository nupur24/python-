# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:36:14 2018

@author: HP
"""

s=raw_input("enter nos : ")
l=s.split()

print l

if all(int(num)>0 for num in l):
    if any(num == num[::-1] for num in l):
        print True
    else:
        print False
else:
    print False





    
        
        















