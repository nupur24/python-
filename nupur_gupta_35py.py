# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:36:56 2018

@author: HP
"""


import pandas as pd

df= pd.read_csv("training_titanic.csv")

print df["Survived"].value_counts()[1]


print df["Survived"].value_counts(normalize = True)

print df["Sex"].value_counts(normalize = True)

print df["Survived"][df['Sex'] == 'female'].value_counts(normalize = True)


print df["Survived"][df['Sex'] == 'male'].value_counts(normalize = True)



