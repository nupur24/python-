# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:19:52 2018

@author: HP
"""

d ={} 
for i in ["a","b","c"]:
    text = input("Enter: ")
    d[i] = text

def main(d):
    total=0
    lst = d.values()
    for i in lst:
        total += check(i)
    return total

def check(num):
    if num in [13,14,17,18,19]:
        return 0
    else:
        return num
print main(d)
    
total = 0    
for i in [1,2,3,4,5,6]:
    print "Before=",total
    total += i
    print "After=",total