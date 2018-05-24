# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:31:43 2018

@author: HP
"""

import urllib2

l="https://www.icc-cricket.com/rankings/mens/team-rankings/test"

p=urllib2.urlopen(l)

from bs4 import BeautifulSoup

soup=BeautifulSoup(p)

alt=soup.find_all('table')

rt=soup.find('table',class_='table')

#col
a=[]
b=[]
c=[]
d=[]
e=[]


for body in rt.findAll("tbody"):
    for row in body.findAll("tr"):
        cells=row.findAll("td")
        a.append(cells[0].find(text=True))
        b.append(cells[1].text.strip())
        c.append(cells[2].find(text=True))
        d.append(cells[3].find(text=True))
        e.append(cells[4].find(text=True))
    
        
import pandas as pd

df=pd.DataFrame(a,columns=["pos"])        
df['team']=b
df['matches']=c
df['point']=d
df['rating']=e

print df


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

