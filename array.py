#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 11:37:58 2018

@author: appiness
"""

#############################################################################
'''1)unique values in array using sorting'''
a=[1,2,3,5,5,7,7,1,8,3,77,5,4,3,4,8,9,6,7,88,55,5,9,9]
b=[]
max=0
a.sort()
print(a)
for i in a:
    if i>max:
        b.append(i)
        max=i
        
print(b)

#############################################################################

##############################################################################
'''2)unique values in an array 
taking user input array'''

def unique(number_array):
    b=[]
    for i in number_array:
        if i not in b:
            b.append(i)
        
    print(b)
'user input array'
number_array = []
number = input("Enter the number of elements you want:")
print ('Enter numbers in array: ')
for i in range(int(number)):
    n = input("number :")
    number_array.append(int(n))
print ('ARRAY: ',number_array)
unique(number_array)
#############################################################################

#############################################################################
'''3)to get the count of a particualar value in an array'''
a=[1,2,3,5,5,7,7,1,8,3,77,5,4,3,4,8,9,6,7,88,55,5,9,9]
x=int(input('enter no.:'))
count=0
for i in a:
    if i == x:
        count+=1
print(count)
#OR
a.count(3)
#############################################################################

#############################################################################
'''4)to count occurence of each no. in ana array'''

a=[1,2,3,5,5,7,7,1,8,3,77,5,4,3,4,8,9,6,7,88,55,5,9,9]
from collections import Counter 
Counter(a)
'print(Counter(a))'
#############################################################################










