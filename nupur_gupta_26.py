# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:04:47 2018

@author: HP
"""




from collections import OrderedDict

od = OrderedDict()
l=[]

while True:
    str1=raw_input("enter : ")
    if not str1:
        break
    t=str1.split(' ')
    
    value=t[-1]
    key=' '.join(l[0:-1])
    od[key] = od.get(key,0) + int(value)
         
for k,v in od.items():
    print k,v        





























