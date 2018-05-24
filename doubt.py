# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:40:32 2018

@author: HP
"""

s= " Python strings are, immutable sequences of characters"
s.find(',')



count=0
for letter in 'snow!':
    print 'Letter # ' +str(count)+ ' is ' +str(letter)
    count +=1
    break



import math
Math.sqrt(16)

x=[1,2,3,4,5,6,7]
n=[9,8,7]
x.extend(n)
print x

x.sort()
print x


print x[1:9:2]

a=(2,3,5,6)
a.insert(2,3)


i=0
while i < 5:
    c=0
    for l in "hello, world":
        c+=1
        if i%2==0:
            break
    print "i "+str(i)+";c is "+str(c)
    i+=1










