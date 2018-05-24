# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:36:20 2018

@author: HP
"""

import pandas as pd

df= pd.read_csv("training_titanic.csv")


df['child']=0

df['Age']=df['Age'].fillna(df['Age'].median())
df['Age']=df['Age'].fillna(df['Age'].mode()[0])

df['child'][df['Age']<18]=1

print df['child']




