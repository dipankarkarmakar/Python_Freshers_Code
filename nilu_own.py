# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:44:50 2018

@author: JYOTI SINGH
"""
'prime no. or not'
num=22
flag=0
for i in range(2,23,1) :
    if (num%i==0):
        flag=1
        break
if (flag==0):
    print('the no. is prime')
else:
    print('the no. is not prime')

    
'''array program'''

#1)    
brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
print(len(brands))

#or

brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
num_brands = len(brands)
print(num_brands)

#2)
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
del colors[4]
print(colors)
colors.remove("blue")
print(colors)
colors.pop(3)
print(colors)
print(colors.pop())
print(colors)


#3)concatenation(combining) of two arrays
birthday=['bat','girlfriend','lamborgini','job','shoes']
del birthday[1]
print(birthday)
christmas=['yacht','job in google','house','food']
total_wishes=birthday+christmas
print('total number\'s wishes=',total_wishes)


'''string program'''
    
#1)
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)

#2)
string = 'programiz'
print('str = ', string)

#first character
print('str = ', string[0])

#last character
print('str[-1] = ', string[-1])

#slicing can only be done in forward direction. No reversing is allowed.
#slicing 2nd to 5th character
print('str[1:5] = ', string[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', string[5:-2])

#3)concatenation in string
str1='hello'
str2='World!'
print('str1+str2=',str1+str2)
print('str1*3=',str1*3)

#4)iteration through string
count=0
a='love lasun love'
for i in a:
    #print(i)
    if (i=='o'):
        count=count+1
print(count,'desired letter found')

'''5)Enumerate-It is a function that writes both the index and value of the
    string. The format to write a enumerate is list(enumerate(dip)) or 
    set(enumerate(dip))'''
    
dip= 'jyoti'
print(list(enumerate(dip)))
print(dict(enumerate(dip)))



dip='jyotii'
print(set(enumerate(dip)))


#to find the length of the string
dip= 'jyoti'
print(len(dip))
print(len('jyoti'))


'''Escaping Inverting Comas'''
# using triple quotes
print('''He said, "What's there?"''')






# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He's \"said\", \"What's there?\"")

#reversing a string
t="avinash"
y=t[::-1]

d='DIPANKAR'
Z=d[::-1]
        
'''count the no. of vowels in a string'''
#1)
string=input("Enter String:")
count=0
for i in string:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        count+=1
print('The no. of vowels is',count,'.')

#2)
def vowels_count(string):
    count=0
    vowels='aeiouAEIOU'
    for i in string:
        if i in vowels:
            count+=1
    print(count)
    return count
    
string='jyoti'
vowels_count(string)


'''to count a given letter in vowel or consonant'''
#1)
def vowels_count(string):
    count=0
    count1=0
    vowels='aeiouAEIOU'
    for i in string:
        if i in vowels:
            count+=1
        else:
            count1+=1
    print(count,':vowels')
    print(count1,':consonant')
    return count
    return count1
    
string=input('Enter Sentence:')
vowels_count(string)

#2)
string1=input("Enter String:")
for i in string1:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        print('The given character is vowel')
    else:
        print('The given character is consonant')


'''HCF & LCM'''










'''Largest Among three nos.'''


a=float(input('Enter First No.:'))
b=float(input('Enter Second No.:'))
c=float(input('Enter Third No.:'))
if (a>=b) and (a>=c):
    largest=a
elif (b>=a) and (b>=c):
    largest=b
else:
    largest=c
    
print('The largest no. between',a,',',b,'and',c,'is',largest,'.')

'''Leap Year'''

year=int(input('Enter Year:'))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print('The year',year,'is a leap year')
        else:
            print('The year',year,'is not a leap year')
    else:
        print('The year',year,'is a leap year')
else:
    print('The year',year,'is not a leap year')

    
'''Multiplication Table'''

num=int(input('Enter Number='))
A=0
for i in range(1,11):
    A=num*i
    print(num,'x',i,'=',A)
    
'''Celsius To Fahrenheit,,,,
Formulae=Celsius*1.8=Fahrenheit-32'''

Celsius=float(input('Enter the desired celsius:'))
Fahrenheit=(Celsius*1.8)+32
print('Celsius=',Celsius,'and Fahrenheit=',Fahrenheit)


        
'''Adding the values of list'''
        
a=[-1.56202800e-01,  -4.01525991e-01 ,  4.22415923e-01,   7.52497193e-01,
    2.25713281e-01  ,1.02988593e-01 , -8.37878481e-02 ,  6.67025801e-04,
    3.13428942e-03,  -3.11004101e-02 , -9.00596119e-03  , 4.59083110e-03,
    6.09096341e-03] 
c=0     
print (type(a)) 
for i in a:
    c=c+i
print(c)     


'''two strings similar'''

l1=input('Enter string:')
l2=input('Enter another string:')
l3=''.join(sorted(l1))
l4=''.join(sorted(l2))
if(l3==l4):
    print('equal')
else:
    print('not equal')
    










                







