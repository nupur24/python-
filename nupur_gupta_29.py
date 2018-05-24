# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:38:12 2018

@author: HP
"""


import re

a=raw_input("enter number : ")

regex = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')

response = regex.match(a)
if response:
    print response.group()
else:
    print "not valid"

  
         


