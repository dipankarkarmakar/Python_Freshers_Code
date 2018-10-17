#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 18:32:13 2018

@author: dipankarkarmakar
"""

f=open("/home/dipankarkarmakar/Desktop/test.txt","r+")
if f.mode == 'r': 
     contents =f.read()
     print (contents)
for i in contents.split():
    if len(i)>=5:
        print(i)
        with open("/home/dipankarkarmakar/Desktop/testdone.txt","a+") as t:
            t.write(i)
            t.write("\n")
        
        
t.close()
f.close()





