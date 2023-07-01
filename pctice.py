# Accept comma-seperated numbers from user and convert it to a list and a tuple
'''
a = input('Enter commaa-seperated numbers: ')
list = a.split(',') # As the coma/dot/#/anything is typed by the user split will seperate that like a list item
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
'''
# print the extension name of file 
'''
d = input('Enter a file name with extension\n')
c = d.split('.')
print('Extension of file is',c[-1])# -1 will print the last list item that is the name opf extension
'''
# Print first and last color from the list 
'''
color_list= ['red','blue','green','yellow','pink']
print(color_list[0],'and',color_list[-1])
'''
#Using calender module
'''
import calendar
y = int(input('Enter the year: '))
m = int(input('Enter the month: '))
print(calendar.month(y,m))
'''
# If-else 
'''
color = input('Enter the color on signal: ')
if color=='red' or color=='Red' :
    print('Stop your vehicle')
elif color=='yellow' or color=='Yellow':
    print('Start your vehicle')
elif color=='green' or color=='Green':
    print('GO!')
else:               
    print('No color matched')
'''
'''
name = input('Enter your name: ')
c = int(input('Enter your class: '))
section = input('Enter your section: ')
a = int(input('Enter marks of english: '))
b = int(input('Enter marks of Scince: '))
c = int(input('Enter marks of Hindi:  '))
d = int(input('Enter mrks of marathi: '))
e = int(input('Enter marks of social science: '))
s = (a+b+c+d+e)
m = ((s/500)*100)
print('Name eof student: ',name)
print('Your class is: ',c)
print('Your Section is: ',section)
print('You got: ',m,'%')
if m >=33 and m <=100:
    print('Pass!')
    if m>=85 and m<=100:
       print('Remark: Very Good')
    elif m>=70 and m<85:
        print('Remark: Good')
    elif m>=33 and m<70:
        print('Remark: Can do better')
    elif m>=0 and m<33:
        print('Remark: Bad')
else:
    print('Fail')
'''
#Acessing through variables
'''
tup = (23,5,7,8,6,4,5)
a,b,c,d,e,f,g = tup
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
'''
#Swaping of two tuples
'''
tuple1 = (25,8,9)
tuple2 = (5,7,9)
tuple1 , tuple2 = tuple2 , tuple1
print(tuple1)
print(tuple2)
'''
'''
tuple1 = (2,9,5)
tuple2 = (tuple1[0],tuple1[1],tuple1[2])
print(tuple2)
'''
#Nested tuples
'''
 a = (4,[22,{'key':'chabi'},6,8],54,99,88)
 a[1][0] = 222
 print(a)
'''
# s = (5,2,5,2,5,2,58,2,8,5,48,5,2,78,5)
# m = s.count(5)
# print(m)

#Write a program to display only those numbers from a list that satisfy the following conditions
'''
The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop

n = [10,280,39,40,549]
for i in n:
    if i>500:
        break
    if i>150:
        continue
    if i%5==0:
        print(i)
print('Done!')
'''
# To print a lsit in reversed order use the reversed function
'''
 list = [34,8,7,69,55,90]
 new_list = reversed(list)
 for i in new_list:
     print(i)
'''
# Write a program to check whether the entered number is prime or not
'''
n = int(input('Enter any of the positive integer: '))
if n>1:
    for i in range(2,n):
        if (n%i)==0:
            print(n,'is not a prime number')
            break
        else:
            print(n,'is a prime number')
 '''
 # Program to reverse an integer
'''
 a = 76542
 b = reversed(a)          
 for i in b:
     print(i)
'''
#Program to print odd indexes through slicing
'''
 my_list = [23,45,3,90,6,12,123,74,58]
 for i in my_list[1::2]:
     print(i,end=' ')
     '''
# find the cube of entered number using loop.
'''
 n = int(input('Enter an integer\n'))
 for i in range(1,n+1):
     print('cube of current number is: ',i**3)
'''
# Sum of n natural numbers
'''
a = int(input('Enter the start no. : '))
b = int(input('Enter the end no.: '))
sum = 0
for i in range(a,b+1):
    sum = sum+i
print('Sum is : ',sum)
'''
#WAP to separate positive and negative number from a list.
'''
x = [2,3,-95,4,5,6,7,-34,-23,-90]
pos = []
neg = []
for i in range(len(x)):
    if x[i] > 0:
       pos.append(x[i])
    elif x[i] < 0:
        neg.append(x[i])
print('Positive integers are: ',pos)
print('Negtive integers are: ',neg)
'''
# print types of data present in a list
'''
x = [2,'Harsh',True,22.35]
ty = []
for i in range(len(x)):
    ty.append(type(x[i]))
    
print('Data types in the list are : ',ty)
'''
# Find and print odd and even numbers from a list using loop
'''
list1 =[12,56,4,8,9,3,77,32]
eve = []
odd = []
for i in range(len(list1)):
    if list1[i]%2 == 0:
        eve.append(list1[i])
    elif list1[i]%2 != 0:
        odd.append(list1[i])
        
print('Even numbers : ',eve)
print('Odd Numbers : ',odd)
'''
#Write a program to fetch only even values from a dictionary
'''
dict1 = {'val1':10,'val2':1,'val3':31,'val4':40,'val5':50,'val6':63}
for i in dict1.values():
    if i%2==0:
        print(i,end=' ')
    else:
        pass
'''
# Find the number of veowels and consonants from a word
'''
n = input('Enter a word: ')
vow = 0
cons = 0
for x in range(len(n)):
    if n[x] in ['a','i','o','u','e']:
        vow = vow + 1
    else:
        cons = cons + 1
print('vowels are: ',vow)
print('Consonants are: ',cons)
'''
#Python program to convert lower letter to upper and upper letter to lower in a string.
'''
n = input("Enter any word: ")
x = []
for i in range(len(n)):
    if n[i].isupper():
        x.append(n[i].lower())
    elif n[i].islower():
        x.append(n[i].upper())
for i in range(len(x)):
    print(x[i],end=' ')
'''
# python program to search a specific word in string
'''
n = input("Enter any Sentence: ")
f = input('Enter the word you want to find in this string: ')
for i in range(len(n)):
    if f in n:
        print(f,': exists in the above sentence')
        break
    else:
        print(f,': does not exists in the above sentence')
        break
'''
# python program for pyramid pattern
'''
n = int(input('Enter the no. of rows: '))
for i in range(n):# Here the no. of rows is defined
    for j in range(i,n):# Here a range from 0 to n is given to print a decereasing triangle
        print(' ',end='')# 1st 0 to 5 spaces will be printed then 0 to 4 then 0 to 3 then 0 to 2 and so on.....
    for j in range(i):# here at the 0th position no star would be printed then 1 star then 2 then 3 then 4 and so on...
        print('*',end='')
    for j in range(i+1):#here the loop starts from one star then 2 then 3 then 4 ......
        print('*',end='')# https://youtu.be/fX64q6sYom0
    print()
'''
# Daimond pattern
'''
n = int(input('Enter the number of rows: '))
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')                                                                                         
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n-1):
        print('*',end='')
    for j in range(i,n):
        print('*',end='')
    print()
'''
'''
dict1 = {
         'harsh': ['habile','Handsome'],
         'mobile':['redmi','Iphone'],
         'place' :['India','Bangladesh']}
dict1[0]='john'
print(dict1)
'''
# Use split method
'''
values = input('Enter some numbers: ')
list1 = values.split(' ')
tup1 = tuple(list1)
print(list1)
print(tup1)
'''
#Display the first and last colors from a given list in Python
'''
colors = input('Enter the names of different colors and seperate them by commas:\n')
l1 = colors.split(',')
print(f"The color entered at first place is: {str(l1[0])}")
print(f"The color entered at last place is: {str(l1[-1])}")
'''
# Display exam date
'''
exam_date = (2,2,21)
print('Exam will start from : %x/%x/%x'%exam_date)
'''
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
'''
l=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        l.append(i)
print(l)
'''
#Write a program which can compute the factorial of a given numbers
'''
n = int(input('Enter any integer: '))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)
'''
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print (d)
'''
#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number
'''
i = map(int,input('Enter comma seperated numbers: ').split(','))
x=list(i)
y=tuple(x)
print(x)
print(y)
'''
#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
'''
lines = []
while True:
    s=input('Enter sequence of line: ')
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print(sentence)
'''
#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically
'''
s=input('Enter words: ').split(" ")
words = [word for word in s]
print(" ".join(sorted(list(set(words)))))
'''
#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
'''
num = input('Enter 4 digit comma seperated binary numbers: ').split(",")
items = [numbers for numbers in num if int(numbers)%5==0]
print(",".join(items))
'''
'''
items_list = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p)
    if not x%5:
        items_list.append(p)
print(','.join(items_list))
'''
