# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:11:40 2018

@author: HP
"""

a=input("enter numbers:")
print a


def add(a):
    c=sum(a)  
    return c


def mul(a):
    return reduce((lambda x, y: x * y),a)
    
def lar(a):    
    c=max(a)
    return c

def sma(a):    
    c=min(a)
    return c

def sor(a):
    c=sorted(a)
    return c

def rd(a):
    c=set(a)
    return list(c)

print(add(a),mul(a),lar(a),sma(a),sor(a),rd(a))

    
    
    



