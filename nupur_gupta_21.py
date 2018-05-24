# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:30:37 2018

@author: HP
"""


import requests

ap = "http://13.127.155.43/api_v0.1/sending"

d={}

for i in ['Phone_Number','Name','College_Name','Branch']:
    d[i]=raw_input("enter "+i+":")

r= requests.post(url=ap,json=d)

p=r.text
print "URL is",p


pn=raw_input("enter phone number :") 
ap1 ="http://13.127.155.43/api_v0.1/receiving?Phone_Number={0}".format(pn)

r1=requests.get(url=ap1)

data=r1.json()
a = r1.text
print a





