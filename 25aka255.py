# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:26:42 2018

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
                 orrrr
    if key in od:
        od[key]=od[key]+int(value)
    else:
        od[key]=int(value)
        
for k,v in od.items():
    print k,v        





l =[]
while True:
    str1=raw_input("enter : ")
    if not str1:
        break
    t=str1.split(' ')
    key=' '.join(t[0:-1])
    
    l.append((key, int(t[-1])))
l.sort()    


def Convert(l, d):
    d = dict(l)
    return d

d = {}
d = (Convert(l, d))

print sum(d.values()














