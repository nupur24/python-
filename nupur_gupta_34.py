# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:08:47 2018

@author: HP
"""

import requests

ap ="https://api.mlab.com/api/1/databases/std/collections/student?apiKey=HbrTgBp-qky1At8fK4qYi6J1S_2SdNGc"

d={}

for i in ['Phone_Number','Name','College_Name','Branch']:
    d[i]=raw_input("enter "+i+":")

r= requests.post(url=ap,json=d)

p=r.text
print "URL is",p


pn=raw_input("enter Name :") 
ap1 = "https://api.mlab.com/api/1/databases/std/collections/student?q={'Name':'"+pn+"'}&apiKey=HbrTgBp-qky1At8fK4qYi6J1S_2SdNGc"

r1=requests.get(url=ap1)
data=r1.json()
a = r1.text
print a


















