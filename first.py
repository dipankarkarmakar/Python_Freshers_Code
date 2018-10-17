# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


j=10
j='C'
print(j)

lll=[12,23,45,56]

i=12
print(i)

'''condition statement'''
if(i==12):
    print("yahoooooooooooo")
else:
    print("NOOOOOOOOOOOOOO")




'''for loop'''    
for i in range(10):
       print(i)

list1=[1,2,3,4,5]
for i in list1:
    if i==3:
        print('found')
        break
        #continue
    print(i)

list=[1,2,3,4,5]
string_1='abc'
for i in list:
    for j in string_1:
        print(i,j,end='|')

'''while loop'''
#1)    
i=0
while(i<10):
    print(i)
    i=i+2
    #or
    i+=2  
    
#2)
x=0
while (x<10):
    if (x==5):
        break  
    print(x)
    x+=1
    
#3)infinite iteration,,,,to cancel the iteration press ctrl+c in console
x=0
while True:
    #if (x==5):
     #   break  
    print(x)
    x+=1
    

    
'''printing the specifying index'''
nilu_list=[1,34,56,99]
print(nilu_list[2])
#this will give error as it is out of index "error: list out of range
print(nilu_list[6])

#about negative indexing

print(nilu_list[-2:])
print(nilu_list[-4:])
print(nilu_list[::-1])


'''length of the list'''

print(len(nilu_list))

'''type'''
print(type(nilu_list))

'''mutable'''
nilu_list[2]=100

'''slicing'''

print(nilu_list[0:3])

'''append vs extend'''

'''*note=append or extend cannot be defined be in other list....ex=
nilu_list=nilu_list.append(500)[wrong]
nilu_list=nilu_list.extend(list2)[wrong]'''

nilu_list.append(500)

list2=[23,34,45]

'''extend=list +list'''
nilu_list.extend(list2)


#to multiply the values in the list doubly in their respective orders
nilu_list=[1,2,3,4]
list_100=[5,6,7,8,9]
print(nilu_list + list_100)
nilu_list.extend(list_100)
print(nilu_list)
nilu_list=nilu_list*2
print(nilu_list)
print(nilu_list*2)
#OR
print(nilu_list+nilu_list)

'''delete,remove,pop,clear,count,sort,reverse,copy'''

#to delete an index no. value or no. of index no. value's 
nilu_list=[1,2,3,4]
del nilu_list[3]
print(nilu_list)
del nilu_list[2]
del nilu_list[0:10]

#to delete the last value of list
nilu_list.pop()
#to delete a particular index no. value
nilu_list.pop(2)

'''assigning value at a specific index'''

nilu_list[1]=200

#to count a no. of times the value are repeated
nilu_list.count(500)

#to arrange the values present in the list in ascending order
nilu_list.sort()
#to arrange the values present in the list in descending order
nilu_list.sort(reverse=True)

'''COPY'''

list4=[1,2,3,4]
nilu_list=[5,6,7,8]
'''deep copy'''
#list4=nilu_list.copy()
'''shallow copy'''
#list4=nilu_list
list4[2]=0
print(nilu_list)
print(list4)

'''deep copy'''

# importing "copy" for copy operations
import copy
 
# initializing list 1
li1 = [1, 2, [3,5], 4]
 
# using deepcopy to deep copy 
li2 = copy.deepcopy(li1)
 
# original elements of list
print ("The original elements before deep copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
 
print("\r")
 
# adding and element to new list
li2[2][0] = 7
 
# Change is reflected in l2 
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
    print (li2[i],end=" ")
 
print("\r")
 
# Change is NOT reflected in original list
# as it is a deep copy
print ("The original elements after deep copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")
    
'''Shallow Copy'''
# importing "copy" for copy operations
import copy
 
# initializing list 1
li1 = [1, 2, [3,5], 4]
 
# using copy to shallow copy 
li2 = copy.copy(li1)
 
# original elements of list
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
 
print("\r")
 
# adding and element to new list
li2[2][0] = 7
 
# checking if change is reflected
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")
print(li2)
#==============================================================================================

#to reverse the values given in the list
nilu_list=[1,5,6,8]
print(nilu_list[::-1])
nilu_list.reverse()
print(nilu_list)
#to clear the values given in the list
nilu_list.clear()
print(nilu_list)

'''insert'''
nilu_list.insert(2,380)

#specifying the value of list2 in nilu_list
list2=[1,2,3,4]
nilu_list=list2

'''iteration of list 
    if (i<100):
        count=count+1thru for loop'''


'''count the number of values which are less than 100'''
nilu_list=[1,2,4,50,100]
count=0
for i in nilu_list:
    if i<100:
        count=count+1
print(count)   

'''to find the even and odd nos. in the list'''
#1)
count=0
count1=0
for i in nilu_list:
    if (i%2==0):
        count=count+1
    else:
        count1=count1+1
print('count of even number',count)
print('count of odd number',count1)

#2)
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print(num," is Even")
else:
   print(num,"is Odd")
   
#3)
count=0
count1=0
for i in range(1,100):
    if (i%2==0):
        count=count+1
    else:
        count1=count1+1
print('count of even number',count)
print('count of odd number',count1)


'''adding 2 lists index wise using zip function'''
l1=[1,2,3,4]
l2=[2,3,4,5]
l4=[]
for a,b in zip(l1,l2):
     l4.append(a+b)
print(l4)
     

        
 ##############################DAY2###########################################

'''
count=0
for i in range(20):
    print(count)
    count=count+1
    print(count)
    print('------------------')
    
'''

nilu_tuple=(12,25,45,42)

print(nilu_tuple[2])

print(nilu_tuple[0:3])
'''
nilu_tuple[2] =34
Traceback (most recent call last):

  File "<ipython-input-6-1306f475cc4b>", line 1, in <module>
    nilu_tuple[2] =34

TypeError: 'tuple' object does not support item assignment
'''
nilu_tuple[2] =34

nilu_tuple=(24,35,48,55)
t2=(12,25,45,89)

t3=t2+nilu_tuple
print(t3)

t2=t2+nilu_tuple
print(t2)

t4=nilu_tuple + t2

'''
del t3[1:10]
Traceback (most recent call last):

  File "<ipython-input-14-44e267fddd3d>", line 1, in <module>
    del t3[1:10]

TypeError: 'tuple' object does not support item deletion
'''
del t3[1:10]
'''
to find the length of the tuple
'''
print('length of the tuple t3 is:',len(t3))

#####SET################

sett={12,25,52,81}
'''to add a value to list'''
sett.add(20)
'''to extend the list'''
'''in set duplicate is not allowed'''
sett.update([20,30,40])

'''to delete a variable from the list & it does not give any error'''
sett.discard(20)
t={25,40,50,60}
t.add(20)
print(t)
t.update([30,56,77])
print(t)
t.discard(56)
print(t)
'''it also delete a value but it gives error'''
sett.remove(25)
print(sett)

sett.discard(100)

sett.remove(100) 

'''Union-it will merge two set values without duplicacy'''
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)

'''Intersection-common in both sets'''
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)

'''Difference'''
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)

'''Symmetric difference-It will remove that which is common in both sets'''

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)


'''DICTIONARY'''
#*note-for integer values we dont use inverted comas

#1)
my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict['age'])

#2)
my_dict={'name':'Jyoti','age':22}
#to update
my_dict['age']=23
print(my_dict)
#to add
my_dict['address']='Khidirpur'
print(my_dict)

#3)
# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

# remove a particular item
# Output: 16
print(squares.pop(4))  

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item
# Output: (1, 1)
print(squares.popitem())

# Output: {2: 4, 3: 9, 5: 25}
print(squares)

# delete a particular item
del squares[5]  

# Output: {2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
# print(squares)


'''Empty list,tuple,set,dict'''

a=[]
print(type(a))

b=()
print(type(a))

c=set()
print(type(a))

d={}
print(type(a))


######EXCEPTION handling###################
'''
In order to handle errors, you can set up exception handling blocks in your code. 
The keywords try and except are used to catch exceptions. When an error occurs within the try block,
 Python looks for a matching except block to handle it.
An exception is an event, which occurs during the execution of a 
program that disrupts the normal flow of the program's instructions.
 In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. 
An exception is a Python object that represents an error.
It helps preventing the code from crashing down.
The code in the finally block will be executed regardless of whether an exception
occurs.
'''


'''if we want to ignore a error'''
sett=[1,2,3,4,110]
try:
   sett.remove(100)
except:
   print('error nhi aaya')      
   


b=0
try:
    a=17/b
except ZeroDivisionError:
    print('bhaiiiiiiiiiiiiiiiiii bach gaye')
     
'''whichever error will occur that only will be taken'''
sett={1,2,3,4,5}   
b=0
try:
    a=17/b
    sett.remove(100)
    
except TypeError :
    print('type error h bhai')    
except ZeroDivisionError:
    print('bhaiiiiiiiiiiiiiiiiii bach gaye')

except KeyError:
     print('hdhd')
except :
    print('akjbsdkjasdjk')  

'''prime no.'''
    
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i/2) == 0:  
               break  
       else:  
           print(num)
           


    
for i in range(10):
    print(i)
#to print the nos. in interval of 2       
for i in range (2,46,2):
    print(i)  
    
'''prime number or not '''
   
n=int(input("Enter lower no.-"))
flag=0
if n>1:
    for i in range(2,n):
        if (n%i==0):
            flag=1
            print(i)
            break
    if (flag==0):
        print('the no. is prime')
    else:
        print('the no. is not prime')
else:
    print('the no. is not prime')

 
'''fibonacci series'''

#1)

a=1
b=1
c=0
print(c)
print(b)
print(a)
for i in range(51):
    c=a+b
    print(c)
    a=b
    b=c
    
#2)

count=3
a=1
b=1
c=0
print(c)
print(a)
print(b)
for i in range(51):
    c=a+b
    if (c<50):
        print(c)
        a=b
        b=c
        count=count+1
    else:
        break
print(count,':Count of fibonacci no. under 50 range')

#3)
a,b=0,1
for i in range(10):
    print(a)
    a,b=b,a+b
    
'''factorial of a number'''

f=1
for i in range (2,6):
   f= f * i
print(f)

'''recursion-factorial no.'''


def fial_number(i):
    if(i==1):
        return(1)
    else:
        return(i*fial_number(i-1))
print(fial_number(5))   

'''Swaping of nos using 3rd variable'''

a=2
b=3
c=b
b=a
a=c
print('a is',a)
print('b is',b)

'''Swaping of nos without using 3rd variable'''

a=3
b=1
b=a+b
a=b-a
b=b-a
print('a is',a)
print('b is',b)

'''Check a no. is positive or negative'''


number = int(input("enter number"))
if (number>0):
    print("positive")
else:
    print("negative")    

'''reversing a string'''
  
arr="dipankar"
print(arr[::-1])
print(arr)
arr=arr[::-1]
print(arr)

#basic itteration
a=[1,2,3,4,56,7,8,9]

for i in a:
    print(i)
    
for i in range (len(a)):
    print(a[i])    


a=[1,2,3,4,56,7,8,9]
a=a[1:3]
print(a)

'''iteration of list of list'''

a = [[1, 3, 4], [2, 4, 4], [3, 4, 5]]
for i in a:
    for b in i:
        print (b)

'''to print two no. from the same index side by side from two different list without zip function'''

a=[1,2,3,4]
b=[2,3,4,5]
for i in range(len(a)):
    print(a[i],b[i],end="|")



'''to find a no. repetition of list in list of list'''

listScore=[[6,7,8],[2,5,6],[6,7,8],[6,7,8]]   
import numpy as np
count = np.all(listScore == np.array([6,7,8]),axis=1).sum()
print(count)






