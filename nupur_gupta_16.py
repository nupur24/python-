# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:40:34 2018

@author: HP
"""







s=raw_input("enter string:")

def translate():
    str2 = ''
    x=['a','e','i','o','u',' ']
    
    for i in s:
        if i in x:
            str2 = str2 + i
            
        else:
            str2 = str2 + (i+'o'+i)
            
    print str2            
            
translate()            
        
            
    
    
    







