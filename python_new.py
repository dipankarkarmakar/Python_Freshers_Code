#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 23:26:42 2018

@author: dipankar
"""

a='sbjcjbdcm sdknsbnsb'
print(''.join(sorted(a)))

'to shuffle a no.'

from random import shuffle
a=[1,5,8,6,45]
shuffle(a)
print(a)

'to print random nos.'
import random
for x in range(10):
  print (random.randint(1,101))
#################################################################  
  
list = ["1", "4", "0", "6", "9"]
list.sort()
print(list)
print(sorted(list))
l=[]
for i in list:
    x=int(i)
    l.append(x)
print(l)
#list = [int(i) for i in list]
l.sort()
print (l)

#####################################
a='jbcsjbsdjbsdjb ghszdjkdfzkj'
print(a.split())


'to count capital letters in a string'

a='sdhvjdshjvsdhjswhHVDSHVSDHHSHHjdhsdh'
count=0
for i in a:
    if i.isupper():
        count+=1
        
print(count)

#######################
a=[1,7,6]
a.sort()
print(a)

'to reverse a string using recursive function'

def reverse(a):
    if len(a)==0:
        return a
    else:
        return reverse(a[1:]) + a[0]  
    
a=str(input('Enter string:'))
reverse(a)


'''to print no. in a given range but when a no. is multiple of 3 then fizz will written instead of the no.
       and buzz when it is multiple of 5 and fizzbuzz when its a multiple of 15'''
    
    
    
for i in range (1,50):
    if (i%3==0 and i%5==0):
        print('fizzbuzz')
    elif i%5==0:
        print('buzz')
    elif i%3==0:
        print('fizz')
    else:
        print(i)
        
        
'to print diagonal values of matrix or list of list'

matrix=[[1,2,3],
   [2,4,5],
   [8,9,6]]
left_diagonal=[]
right_diagonal = []

for i in range(len(matrix)):
    left_diagonal.append(matrix[i][i])
print(left_diagonal,'-left diagonal')


for row in range(len(matrix)):
    col = len(matrix) - row - 1  
    right_diagonal.append(matrix[row][col])
    
print (right_diagonal,'-right diagonal')   























