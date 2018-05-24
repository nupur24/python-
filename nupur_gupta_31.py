# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:27:50 2018

@author: HP
"""




import re

a=raw_input("enter email : ")

regex = re.compile('[a-z0-9_-]+@[a-z0-9]+\.[a-z]{2,4}$')

response = regex.match(a)
if response:
    print response.group()
else:
    print "not valid"
