# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:04:24 2018

@author: HP
"""





from pymongo import MongoClient

#import json

client = MongoClient('localhost', 27017)
mydb = client.db_Forsk



def add_client(n,s_email,r,b,a):

    unique_client = mydb.forsk_clients.find_one({"Email":s_email}, {"_id":0})
    if unique_client:
        return "Client already exists"
    else:
        mydb.forsk_clients.insert(
                {
                "name" :n,
                "age" : a,
                "roll Number" : r,
                "branch" : b,
                "Email":s_email,
                
                })
        return "Client added successfully"

def view_client(s_email):
    user = mydb.forsk_clients.find_one({" Email":s_email}, {"_id":0})
    if user:
        n= user["name"]
        b = user["branch"]
        r = user["roll Number"]
        a = user["age"]

        
        return { " Name":n,"branch":b,"roll Number":r," age":a}
    else:
        return "Sorry, No such user exists"

k = input("Enter: ")
for i in range(k): 
    n = raw_input("Enter Name: ")
    s_email = raw_input("Enter  Email: ")
    r = raw_input("Enter roll Number: ")
    b = raw_input("Enter branch: ")
    a = raw_input("age: ")
    
    print add_client(n,s_email,r,b,a)

user = raw_input("Enter Email to find: ")
user_data = view_client(user)

print user_data




