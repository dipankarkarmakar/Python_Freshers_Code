#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 12:31:14 2018

@author: dipankarkarmakar
"""

def name(a,b):
    c=int(a)+int(b)
    print(c,'I am in the print')
    
import sys 
    
if __name__=='__main__':
    t=sys.argv[0]
    print(t,'0 me kya hota h bhaiya')
    u=sys.argv[1]
    y=sys.argv[2]
    print(u)
    print(y)
    name(u,y)