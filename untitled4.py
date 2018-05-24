# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:16:32 2018

@author: HP
"""

while True:
    s = raw_input("enter string : ")
    if not s:
        break

    if s.count("@")!=1 and s.count(".")!=1:
        print "invalid"
    else:    
        s = s.split("@")
        #print s
        usr = s[0]
        print usr
        web_ext = s[1].split(".")
        print web_ext
        if len(web_ext) == 2:
            web,ext = web_ext
            #print web
            #print ext
            print "valid"
        else:
            print "Failed"









      
        
        
        