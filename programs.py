# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''Armstrong no.'''
#1)
lower=int(input('Enter Lower no.:'))
upper=int(input('Enter Upper no.:'))
for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    A=num
    while A>0:
        R= A%10
        sum=sum+R**order
        A=A//10
    if(num==sum):
        print(num)
print('All the above nos. in the range',lower,'and',upper,'are armstrong no.')

#2)        
num=int(input('Enter no.:'))
order=len(str(num))
sum=0
A=num
while A>0:
    R=A%10
    sum=sum+R**order
    A=A//10
if(num==sum):
    print(num,'is an armstrong number')
else:
    print(num,'is not an armstrong number')

'''Palindrome'''
#1)
a=int(input('Enter no.:'))
num=str(a)
t=num[::-1]
if (num==t):
    print('The given no. is palindrome.')
else:
    print('The given no. is not palindrome')
    
#2)
a=input('Enter string:')
t=a[::-1]
if (a==t):
    print('The given no. is palindrome.')
else:
    print('The given no. is not palindrome')
    
#3)
flag=0
A=input('Enter the string:')
B=len(A)
for i in range(B):
    if (A[i] != A[B-i-1]):
        flag=1
        break
if (flag==0):
    print('Palindrome')
else:
    print('Not Palindrome')
    
    
    
'''print no. without using loop with the help of recursive function'''

def printNos(n):
    if n > 0:
        printNos(n-1)
        print(n, end=' ')
n=int(input('Enter no.:'))
printNos(n)

'''Reversing a Digit'''
a=[1,2,3]
a=int(input('Enter digit:'))
#b=(str(a)[::-1])
a.reverse()
#b=str(a)
#t=b[::-1]
print(a)


'''To print a string separately in a list'''
'''list comprehension'''

#using loop
a=input('Enter string:')
l=[]
for i in a:
    l.append(i)
print(l)

#using list comprehension
a=input('Enter a string:')
l= [ i for i in a ]
print(l)

#conditional list comprehension
a=int(input('Enter range:'))
number_list = [ x for x in range(a) if x % 2 == 0]
print(number_list)


#Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)           

#if...else With List Comprehension
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)


'''how to find max. no. in a list without using sort'''
l=[19,12,15,1,10,9]
max=0
for i in l:
    if i>max:
        max=i
print(max)


'''find a fib no. which is just less than the given user defined no.'''

a=1
b=1
c=0
up=int(input('Enter no.:'))
max1=0
for i in range(up):
    if (up>(a+b)):
        c=a+b
        a=b
        b=c
        max1=c
    else:
        break
print(max1)

#2)
a,b=0,1
for i in range(10):
    print(a)
    a,b=b,a+b
    
    
'''to split a sentence'''

sent='this is my name'
print(sent.split())
for i in sent.split():
    print(i)




'''to count a no. of character in a given sentence'''
'''
count=0
sent='this is my name'
a=input('enter letter:')
for i in sent:
    if i==a:
        count+=1
print(count)
'''
count=0
sent=input('Enter sent:')
a=input('Enter word:')    
for i in sent.split():
    for j in i:
        if (j==a):
            count+=1
print(count) 

#or
'''to count a no. of character in a given sentence if the character'''
a=input('Enter a word:')
sentence=input('Enter Sentence:')
print(sentence.count(a))



'''to count a particular word in a given sentence'''

count=0
sent='my name is nilu nilu nilu nilu karmakar nilu'
b='nilu'
for i in sent.split():
    if i==b:
        count+=1
print(count)
    
'''to count each words in a given sentence'''

count=0
count1=0
count2=0
count3=0
count4=0
sent='my name name name is nilu nilu nilu nilu karmakar nilu karmakar'
b='nilu'
a='karmakar'
c='name'
d='my'
e='is'
for i in sent.split():
    if i==b:
        count+=1
    if i==a:
        count1+=1
    if i==c:
        count2+=1
    if i==d:
        count3+=1
    if i==e:
        count4+=1
        
print('\"nilu\" repeats ',count,' times')
print('\"karmakar\" repeats ',count1,' times')
print('\"name\" repeats ',count2,' times')
print('\"my\" repeats ',count3,' times')
print('\"is\" repeats ',count4,' times')

'''How to iterate in Dictionary'''
#1)
d = {'x': 1, 'y': 2, 'z': 3} 
for i in d:
    print(i)
#2)
d = {'x': 1, 'y': 2, 'z': 3} 
for i,j in d.items():
    print(i,j)

'''sorting a dictionary by 1)value and 2)key'''
    
from collections import Counter
counter = Counter({'A': 10, 'C': 5, 'H': 7, 'X': 15, 'z':12})
'''sorting value'''
print(counter.most_common())
'''sorting by key'''
print(sorted(counter.items()))


'''Lambda operator'''
#1)
sum= lambda x,y: x + y
print(sum(1,1))

#2)Wrong
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print( Fahrenheit)
#[102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print( C)
#[39.200000000000003, 36.5, 37.300000000000004, 37.799999999999997]

'''Exception Handling'''

import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)

'''binary no. to decimal'''

a=int(input('Binary no.:'))
c=str(a)
b=len(c)
z=0
for i in range(1,b+1):
    z=z+ int(c[i-1])*2**(b-i)
print(z)


print("Enter 'x' for exit.")
binary = input("Enter number in Binary Format: ")
if binary == 'x':
    exit()
else:
    decimal = int(binary, 2)
    print(binary,"in Decimal =",decimal)    

decimal_number=12
binary="{:b}".format(decimal_number)
print(binary)



'''Write a Python program that accepts a string and calculate the number of digits and letters.'''
###########################WWWWWWRRRRRRROOOONNGGGGGGG#############
import re
l = list()
d = list()
count=0
count1=0
s = str(input('Enter a string: '))
for i in s:
    if re.search('[A-Z]',s):
        l.append(i)
        count+=1
    elif re.search('[a-z]',s):
        l.append(i)
        count+=1
    elif re.search('[0-9]',s):
        d.append(i)
        count1+=1
print('Letters:',len(l),'\n','Digits:',len(d))
print(count,'=no. of letters','and',count1,'=no. of digits.')


'''type'''
x=3
print(type(x))

points = [(3,7),(45,23),(77,32),(3,7)]
print(type(points))

l=[1,'z']
print(l[1])
print(type(l))


'''properties of count'''
count=0
for i in range(0,10):
    count+=2
    print(count)

'''numpy lib'''
#1)
import numpy as np
cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
c=np.array(cvalues)
print(c)
print('In Fahrenheit=',c*1.8+32)
import matplotlib.pyplot as plt
plt.plot(c)
plt.show()

#2)
import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))
b = np.array([6, 7, 8])
print(b)
print(type(b))


l='zajbsjbdcbjjbkds'
print(''.join(sorted(l)))
print(l)

'''occurence of each character in a given sentence(understand it from bhaiya'''
a='sentence sentence'
b=dict((letter,a.count(letter)) for letter in set(a))
print(b)


'''Anagram or not program-
    (Anagram meaning-a word, phrase, or name formed by rearranging the letters of another,
    such as spar, formed from rasp.)'''

s1=input("Enter first string:")
s2=input("Enter second string:")
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")

'''sorting of a string'''

a = 'ZENOVW'
print(''.join(sorted(a)))

'''Elaboration of sorting of string'''

a = 'ZENOVW'
b=sorted(a)
print(b)
c=''.join(b)
print(c)

'''sorting in a list'''

l=['g','a','d','b']
l2=[5,4,105,54,78]
l.sort()
l2.sort()
print(l,l2)

'''Validity Check of a Password
re-A regular expression is a special sequence of characters that helps you match or find 
other strings or sets of strings, using a specialized syntax held in a pattern. 
Regular expressions are widely used in UNIX world. The module re provides full 
support for Perl-like regular expressions in Python.'''

import re
a=input('Enter Password:')
for i in a:
        if len(a) < 8:
            print("Make sure your password is at lest 8 letters")
            break
        elif re.search('[0-9]',a) is None:
            print("Make sure your password has a number in it")
            break
        elif re.search('[A-Z]',a) is None: 
            print("Make sure your password has a capital letter in it")
            break
        elif re.search('[a-z]',a) is None: 
            print("Make sure your password has a small letter in it")
            break
        elif re.search('[!@#$%&*^]',a) is None:
            print('Make sure password has atleast one any of \'!@#$%&*^\' symbol in it')
            break

        else:
            print("Your password seems fine")
            break


'''wrong-to find a no. letters and number in a string'''


x=input('Enter Sentence:')
c=x.split()
d=str(c)
digit = 0
letters = 0
space = 0
other = 0
for i in d:
    for j in i:
        
        if i[j].isalpha():
            letters += 1
        elif i[j].isnumeric():
            digit += 1
        elif i[j].isspace():
            space += 1
        else:
            other += 1
print(digit,'',letters,'',space,'',other)




with open ("file.txt","w+") as f:
    f.write('Avinash')
    
    
    
    

'''*******writing two strings alternatively of uneven length'''
def alt(s,t):
    if not (s and t):
        return s+t
    else:
        return s[0]+t[0]+alt(s[1:],t[1:])
    
x=alt('hello','bye')
print(x)


        

       



    





