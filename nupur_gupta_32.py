# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:05:13 2018

@author: HP
"""

import re

a=raw_input("enter  : ")

regex = re.compile(r'^[4-5][0-9]-[0-9]-[0-9]-[0-9]d{16}')

response = regex.match(a)
if response:
    print response.group()
else:
    print "not valid"



