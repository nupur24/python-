# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:04:24 2018

@author: HP
"""

p=raw_input("enter string : ")
def c(p):
    a="abcdelghijklmnopqrstuvwxyz"
    pl=""

    for char in p:
        if char in a:
            pl+= char
            
    for char in a:
        if char not in p:
            return False
    return True
c(p)

if c==True:
    print ("panagram")
else:
    print ("not panagram")    
    
        







