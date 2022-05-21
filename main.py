# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# a = 5

#print(type(a))

#b=" You are Beautiful"
#c=" But i am smart"

#print (b+c)

#a=23
#b=2

#c=a+b
#d=a*b

#if c==d:
   # print("product and sum are equal")
#else:
    #print ("product and sum are different")

#num = float (input("Enter a number: "))

#if num > 0:
    #print("Positive number")
#elif num == 0:
    #print("Zero")
#else:
    #print("Negative number")

#for i in range (1,6,1):
   # print(i)

#password =str(input("enter your password:"))

#while password != 'secret':
    #print('invalid password')
   # password = input()
    #print("valid password"




## if else excercise 1:

'''a= int(input("enter 1st number: "))
b= int (input("enter 2nd number: "))

c = a+b
if c > 20:
    print("the amount is greater than 20")
else:
    print (" the ammount is less than 20")'''

##finding vowel 3

'''word= str(input("Enter word: "))
vowel= "a"

if vowel in word:
    print("Vowel a is in the word", word)
else:
    print("there is no vowels")'''

#Write a program to multiply two numbers in the range ending with the number 10. At the beginning of the program ask the user if he wants to multiply the numbers. If user answers yes, enable input and multiplication. If he answers no, enable exit out of the program.

'''a = input("Do you wish to input and multiply thr numbers? ")

if a =='yes':
    print (" Enter your 1st number less than 10: ")
    firstno = int(input())
    print("Enter your 2nd no also less than 10: ")
    secondno =int(input())
    result= firstno * secondno
    print("the result is:", result)
else:
    print("Exit the program")'''

##Write a program that will allow the user to enter the sides of a triangle. The program prints the
#sides of the triangle in the order in which they were entered by the user. The program checks if
#such a triangle exists. If there is then it is checked whether the triangle is equilateral, isosceles or
#scalene. After checking, the program prints a notification about the existence of such a triangle
#and the type of triangle, otherwise it prints that the triangle does not exist.

#HINT: checking the existence of the geometric shape of a triangle. If the sum of the two
#corresponding sides is greater than the third page, then the triangle exists. If the sum of two
#sides of a triangle is less than the third, it means that the triangle does not exist. For example:
#a=2 b=2 c=2 => 2+2>2 meaning the triangle exists
#a=1 b=1 c=6 => 2+2<6 meaning the triangle does not exist

'''a=int(input("enter 1st side:"))
b=int(input("enter 2nd side:"))
c=int(input("enter 3rd side:"))

print("First Page:",a)
print("Second Page:",b)
print("third Page:",c)

if a+b>c:
    print("triangle exist")
else:
    print("triangle does not exist")
if a==b==c:
    print("Isoscales")
    a=b
    print("equilateral")
    b=c
    print("equilteral")
    c=a
    print("equilteral")
else:
    print("scale")'''

#Elif statement

###1. Create a program that will perform the following operations for the entered two numbers:
#addition, subtraction, multiplication and division. Initially, it is necessary to allow the user to
#enter two numbers, then select the operation by selecting the character of that operation
#(+, -, *, /).


'''a= int(input("Enter your 1st number:"))
b= int(input("Enter your 2nd nzmber"))

c = input("Enter operation")

if c == '+':
    result= a+b
    print(result)
elif c== '-':
    result= a-b
    print(result)
elif c== '*':
    result=a*b
    print(result)
elif c=='/':
    result=a/b
    print(result)
else:
    print("no operation")'''

##Write a program that will allow the user to enter a desired number. The entered number should
#be divided by 3. Then if the remainder of the division with number 3 is: equal to zero print
#“blue”, equal to 1, print “red”, equal to 2, print “green”, equal to 3, print “purple”, otherwise
#print “yellow”.


'''a= int(input("Enter a number:"))

c=a%3

if c ==0:
    print("blue")
elif c == 1:
    print("red")
elif c== 2:
    print("green")
elif c== 3:
    print("purple")
else:
    print("yellow")'''

#FOR Statements exercises:
#Using FOR loop print fist 10 numbers, but exclude number 7.

'''for x in range(11):
    if (x == 7):
        continue
    print(x,end=' ')
print("\n")'''

# Write a program which will generate multiplication table of numbers up to 10



'''for i in range(1,11):
    for j in range(1,11):
        print(i*j)'''

#Calculate sum of odd and even numbers in a list in python

'''NumList = []
Even_Sum = 0
Odd_Sum = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] % 2 == 0):
        Even_Sum = Even_Sum + NumList[j]
    else:
        Odd_Sum = Odd_Sum + NumList[j]

print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
print("The Sum of Odd Numbers in this List =  ", Odd_Sum)'''

'''from random import randint
import itertools

flip= int(input("input desired numbe: "))

for i in range(flip):
    result= random(0,1)
    print(result)
    if result == 0:
        print("head")
    else:
        print ("tail")'''

'''class Person:
    def walk(self):
        print("walk")

P = Person()

P.walk()'''


str1 = "Race"
str2= "Care"

# convert both the strings into lowercase
str1 = str1_lower()
str2 = str2.lower()

# check if length is same
if(len(str1) >= len(str2)):

# sort the strings
sorted_str1 = sorted:str1
sorted_str2 = sorted(str2)
# if sorted char arrays are same
if sorted_str1 == sorted_str2:
         print(str1 + " and " + str2 + " are anagram.")
     else:
        print(str1 + " and " & str2 + " are not anagram.")

else
    print(str1 +  and  + str2 + " are not anagram.")


#new code operation