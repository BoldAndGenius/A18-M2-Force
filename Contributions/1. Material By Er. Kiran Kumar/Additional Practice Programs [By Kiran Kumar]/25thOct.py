# Revision - Solve 100 Programming Questions in 9 Hours 

# Question - 1
# Revision Series - Program to add two numbers. 

# Method - 2: Using Predefined Variables
num1 = 10
num2 = 30
sum = num1 + num2
print(f"Sum of {num1} + {num2} is {sum}")


# Method - 2: Using User Input  

num1 = float(input("Enter a Number 1 : "))
num2 = float(input("Enter a Number 2 : "))
sum = num1 + num2 
print(f"The Sum of {num1} + {num2} is {sum}")



# Question - 2 
# Python Program to Print Hello World 

print("Hello World")




# Question - 3
# Python Program to find the square root of a number 

# Method - 1: Using Exponentiation 

num = int(input("Enter a Number: ")) # 64
square_root = num ** 0.5   # or    num ** (1/2)
print(f"The Square Root of {num} is {square_root}")



# Method - 2: Using Math Module 
import math 
num = int(input("Enter a Number : "))
square_root = math.sqrt(num) # math is a module name
print(f"The Square of {num} is {square_root} ")






# Question - 4
# Python Program to Calculate the Area of a Triangle 
height = int(input("Enter a Height : "))
base = int(input("Enter the Base : "))
area = (0.5) * base * height   # or   (1/2) * base * height
print(f"The Area of Triangle is {area}")




# Question - 5
# Python Program to Solve Quadratic Equation 
# cmath -- complex math -- to find the square root   (cmath's sqrt function works with both real & complex numbers)  but (math's sqrt function will only work with real numbers.)
# Use math.sqrt() when working with real numbers and you don't expect negative inputs.
# Use cmath.sqrt() when you may encounter negative numbers or need to work with complex numbers.


import cmath  # complex math # for complex mathematics use this
# quadratic equation -- ax**2 + bx + c = 0,  a,b,c are real numbers  and a != 0
a = float(input("Enter any Number (a != 0) : "))
b = float(input("Enter any Number : "))
c = float(input("Enter any Number : "))
# formaula for descriminant
d = b**2 - 4*a*c 
# roots
root1 = (-b + cmath.sqrt(d))/ 2 * a 
root2 = (-b - cmath.sqrt(d))/ 2 * a 
print(f"The Roots of the equation are {root1} & {root2}")





'''
The primary difference between the `sqrt` function in the `math` and `cmath` modules is in how they handle different types of numbers:

1. **`math.sqrt()` (from the `math` module)**:
   - It only works with **real numbers** (non-negative numbers).
   - If you pass a negative number to `math.sqrt()`, it will raise a `ValueError` because the square root of a negative number is not a real number.
   - It returns a **float**.

   Example:
   ```python
   import math
   print(math.sqrt(16))  # Output: 4.0
   print(math.sqrt(-16)) # Raises ValueError
   ```

2. **`cmath.sqrt()` (from the `cmath` module)**:
   - It works with both **real and complex numbers**.
   - If you pass a negative number, it returns a **complex number** instead of raising an error.
   - It returns a **complex number** in the form of `a + bj`, where `a` is the real part and `b` is the imaginary part.

   Example:
   ```python
   import cmath
   print(cmath.sqrt(16))  # Output: (4+0j)
   print(cmath.sqrt(-16)) # Output: 4j (imaginary number)
   ```

In summary:
- Use `math.sqrt()` when working with real numbers and you don't expect negative inputs.
- Use `cmath.sqrt()` when you may encounter negative numbers or need to work with complex numbers.

'''




# Question - 6
# Python Program to Swap Two Variables 

# Method - 1 : Using Third Variable 
num1 = 10
num2 = 20
print("Before Swapping")
print(f"num1 -> {num1} and num2 -> {num2}")
temp = num1 
num1 = num2 
num2 = temp
print("After Swapping")
print(f"num1 -> {num1} and num2 -> {num2}")


# Method - 2: Using Multiple Variable Creation (Without Using Third Variable)

num1 = 10
num2 = 20
num1, num2 = num2,num1 
print(f"num1 -> {num1} and num2 -> {num2}")






# Question - 7 
# Python Program to Generate Random Number 

import random   # using random module 
print(random.randrange(1,20))


num = random.randint(0,10)  # random integer from the range of numbers  -- 0 & 10 will be included
print(num)



# Question - 8
# Mimic Dice Roll Using Random Module

import random
num = random.randint(1,6)
print(num)


# Question - 9
# Python Program to convert Kilometers to Miles.
# 1 kilometer = 0.621371 Mile 

km = float(input("Enter Your Value in Km: "))
mile = 0.621371 * km 
print(f"{km} Km will be {mile} miles")


# Question - 10
# Python Program to convert Celsius to Fahrenheit 
# Formula -
# T(F) = (9/5 * T(C)) + 32  
# 9/5 can also be written as 1.8 
# 0 Degree Celsius = 32 Fahrenheit    [Put T(c) = 0, you will get the result.]

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = ((9/5) * celsius) + 32  # you can use use 1.8 as well at the place of 9/5
print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")



# Question - 11
# Python Program to check if a Number is Positive, Negative or 0. 

# Using Variables & Conditionals Statements 
# zero is neutral (not a positive, not negative)

num = int(input("Enter a Number : "))
if num>0:
   print("Positive Number.")
elif num == 0:
   print("Zero")
else:
   print("Negative Number.")




# Question - 12 
# Python Program to Check if a Number is Odd or Even. 

# Even Number -- Perfectly divisible by 2. (When divide by 2, remainder should come 0) -- 2 ke table me aane wale sare number including 0 is an even number.
# rest remaining numbers are odd, 2 se divide karne ke baad perfect remainder nahi dete hai...vo decimal ke badd bhale hi 0 de dete hai...but perfectly 0 nahi dete hai. ...without decimal value....that numbers are called odd. 
# Jaha pe perfect remainder 0 aa jai....2 se divide karne ke baad.

# Using Variable, Modulus Operator & Conditional Statements. 

# Modulus Operator -- use to find the remainder.  

num = int(input("Enter a Number : "))
if num % 2 == 0:
   print("Even Number.")
else:
   print("Odd Number.")
   
   
   
# Question - 13 
# Python Program to check leap year 

# noraml year has 365 Days 6 Hours.
# in leap year , we have 366 Days. ----- ones in 4 years. (in February, we get 29 days instead of 28 days.).

# 1996 - Leap Year.  ----- for non centurian year (case - 1),  year % 4 ==0 and year % 100 != 0
# 2000 - Leap Year. ----- for centure year (case - 2),  year % 100 == 0 and year % 400 == 0
# 2004 - Leap Year.
# 2006 - Not a Leap Year.
# 2024 - Leap Year.

year = int(input("Enter an Year : "))
if year%4 == 0:
   if year%100 == 0:
      if year % 400 == 0:
         print("Leap Year.")
      else:
         print("Not a Leap Year.")
   else:
      print("Leap Year.")
else:
   print("Not a Leap Year. ")
   
   
   
   
# Question - 14 
# Python Program to find the Largest Among Three Numbers 

# Using Conditional Statements & Operators. 

num1 = int(input("Ente a Number 1 : "))
num2 = int(input("Enter a Number 2 : "))
num3 = int(input("Enter a Number 3 : "))

if (num1>num2) and (num1>num3):
   print(f"{num1} is greatest.")
elif (num2>num3):
   print(f"{num2} is Greatest.")
else:
   print(f"{num3} is Greatest.")
   
   
   
# it can also be write like this 

num1 = int(input("Ente a Number 1 : "))
num2 = int(input("Enter a Number 2 : "))
num3 = int(input("Enter a Number 3 : "))

if (num1>num2) and (num1>num3):
   print(f"{num1} is greatest.")
elif (num2>num1) and (num2>num3) :
   print(f"{num2} is Greatest.")
else:
   print(f"{num3} is Greatest.")





# Question - 15 
# Python Program to check Prime Number 

'''
REVISE REVISE REVISE REVISE REVISE   (******)

'''

# prime number -  1 and itself only. 
# eg. 3, 5,7,11,13,17.....


# Using Variables, Operators, For Loop & Conditional Statements

# 1 is neither prime nor composite -- 1 se to sare hi number divisible hote hai.

number = int(input("Enter a Number : "))
prime = True

if number == 1:
   print("1 is not a prime number.")
   
else:
   for num in range(2,number):
      if number%num == 0:
         prime = False
         
   if prime == True:
      print(f"{number} is a Prime Number.")
   else:
      print(f"{number} is not a Prime Number.")
      
  
  
      
# 2nd Logic 

num = int(input("Enter a Number : ")) 

if num == 1:
   print("Not a Prime Number.")
elif num > 1:
   for number in range(2,num):
      if num % number == 0:
         print("Not a Prime Number")
         break 
      else:
         print("Prime Number.")
         break 
elif num < 1:
   print("Kindly enter Positive Number only.")   # negative numbers can't be a prime number. 
else:
   print("Invalid!")
   
   






# Question - 16 
# Python Program to Print all Prime Numbers in an Interval 

"""
Revise Revise Revise Revise Revise  (******** VVIP  )
"""

# start = 1 
# end = 6
# output = 2, 3, 5

# Wrong Logics -- not done! 

# start = int(input("Enter the Starting number : "))  # 1
# end = int(input("Enter the Ending Number : "))  # 6

# while start <= end:
#    for num in range(2,start):
#       if start % num:
#          print(start,end=" ")
#    start = start + 1



# Where is the mistake in this logic --- (********)
# start = 1
# end = 10 

# while start <= end:
#    # start = 1
#    for num in range(2,start):
#       if start % num != 0:
#          print(start)
#    # print(start)
#    start = start + 1
   
   
   
   
# Where is the problem in this ? 
# lower = int(input("Enter a Lower Limit : "))
# higher = int(input("Enter the Higher Limit : "))
# for num in range(lower,higher+1):
#    if num > 1:
#       for number in range(2,num):
#          if num % number == 0:
#             continue
#          else:
#             print(num)
   
   

lower = int(input("Enter a Lower Limit : "))  # 10
higher = int(input("Enter the Higher Limit : "))  # 20
for num in range(lower,higher+1):
   if num > 1:
      for number in range(2,num):
         if num % number == 0:
            break  # it's a not prime, therfore break the loop
      else:
         print(num)  # we have to print the number 
   else:
      print("Kindly Enter Positive Number greater than 1.")






# Question - 17
# Python Program to find the factorial of a number 

# 0! = 1
# 1! = 1
# 2! = 2*1
# 3! = 3*2*1
# Number multiplied by it's one decremented number till 1. 

# we can't find factorial of a negative number. 


# Factorial Using For Loop 
num = int(input("Enter a Number : "))
factorial = 1
if num < 0:
   pass
elif num == 0 or num == 1:
   print(1)
else:
   for number in range(1,num+1):
      factorial = factorial * number
   print(factorial)
   
# Factorial Using While Loop 

num = int(input("Enter a Number : "))
if num < 0:
   pass
elif num == 0 or num == 1:
   print(1)
else: 
   factorial = 1
   while num > 0:
      factorial = factorial * num 
      num = num - 1
   print(factorial)
   
# Factorial Using Recursion 

# 5! = 5*4*3*2*1 

# 5! = 5 * 4!         
# 4! = 4 * 3! 
# 3! = 3 * 2! 
# 2! = 2 8 1! 

def factorial(num):
   if num < 0:
      print("Kindly Enter Positive Numbers.")
   elif num == 0 or num == 1:
      return 1 
   else:
      return num * factorial(num-1)
result = factorial(5)
print(result)




# Question - 18 
# Python Program to display the multiplication table 

# Using For Loop
num = int(input("Enter a number for which you want to print the table : ") )
for n in range(1,11):
   print(f"{num} X {n} = {num*n}")
   
# Using While Loop

num = int(input("Enter a Number : "))
number = 1
while number <= 10:
   print(f"{num} X {number} = {num*number}")
   number = number + 1
   
                
                
                
                
# Question - 19
# Python Program to Print the Fibonacci Sequence 
# 0,1,1,2,3,5,8 
# [Revise Revise Revise Revise Revise  (*******)]




# Using For Loop 

num1 = 0
num2 = 1

num = int(input("Enter a number till which you want the fibonacci series : "))

if num == 1:
   print(num1)
elif num == 2:
   print(num1,num2, sep=" , ")
else: 
   print(num1,num2,sep=" , ", end=" , ")
   for number in range(1,num-1):
      num3 = num1 + num2 
      num1 = num2 
      num2 = num3 
      print(num3, sep=" , ",end=" , ")
   
   

# Using While Loop  


num1 = 0
num2 = 1

num = int(input("Enter a number till which you want to print the fibonacci series : "))

if num == 1:
   print(num1)
elif num == 2:
   print(num1,num2, sep=" , ")
else:
   number = 1
   print(num1,num2, end=" , ", sep=" , ")
   while number <= num - 2:
      num3 = num1 + num2
      num1 = num2 
      num2 = num3 
      print(num3, sep=" , ", end=" , ")
      number = number + 1






# Using Recursion 
def fibonacci(num):
   if num == 1:
      return 0 
   elif num == 2:
      return 1 
   else:
      return fibonacci(num-1) + fibonacci(num-2)
result = fibonacci(5)
print(result)






# Question - 20 
# Python Program to check Armstrong Number 

 # 153 = (1*1*1) + (5*5*5) + (3*3*3) == 153  # cube because the number of digits are 3
 # 42 = (4*4) + (2*2)  # square because the number of digits are 2
 
 
num = int(input("Enter a Number : "))  # 123 
temp1 = num
temp2 = num 

length = 0 
while temp2 > 0:
   last = temp2 % 10 
   length = length + 1
   temp2 = temp2 // 10 
# print(length)

# above while loop code can also be replaced with typcasting concept
# length = len(str(temp2))

armstrong = 0
while num > 0:  # 123 > 0
   last = num % 10   # 3
   armstrong = armstrong + last ** length  # armstrong = 0 + 3 ** 3 = 27 
   num = num // 10
   
if temp1 == armstrong:
   print("Armstrong Number.")
else:
   print("Not an Armstrong Number.")
   
   
   
   


# Question - 21
# Write a function to calculate the sum of all digits in a given number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        last = n % 10 
        sum = sum + last 
        n = n // 10 
    print(sum)

n = int(input("Enter a Number : "))   
sum_of_digits(n)



# Question - 22
# Write a function to check if a number is prime within a given range. 

def is_prime_in_range(n, start, end): # 10, 2, 5
    prime = True 
    for num in range(start,end+1):
        if n % num != 0:  # 10 % 2, 10%3, 10%4, 10%5
            break
        else:
            prime = False 
    if prime == True:
        return True 
    else:
        return False 
print(is_prime_in_range(10,2,5))



# Question - 23 
# Write a function to check if an integer is divisible by 5. 

def is_divisible_by_five(n):
    if n % 5 == 0:
        return True 
    else:
        return False
print(is_divisible_by_five(10))


# Question - 24
# Write a function to check if the entered integer is odd or even. 

def odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(odd_even(23))
   



# Question - 25
# Write a function to check if a person is eligible to vote.


def eligible_to_vote(age):
    if age>=18:
        return True 
    else:
        return False 
     
result = eligible_to_vote(20)
print(result)




# Question - 26
# Write a function to check whether a student passed or failed his/her examination.

def pass_fail(score):
    if score >= 50:
        return "Passed"
    else:
        return "Failed"
result = pass_fail(60)
print(result)



# Question - 27 
# Write a function to add 10 to the given number. 

def add_ten(n):
    return n+10
result = add_ten(10)
print(result)


# Question - 28
# Write a function to convert a given length from meters to centimeters. 

def meters_to_centimeters(meters):
    return meters * 100 
result = meters_to_centimeters(10)
print(result)


# Question - 29
# Write a function to find the largest of two numbers.
# REVISE REVISE REVISE REVISE  REVISE REVISE  


def find_largest(num1, num2):
    if num1 > num2:
        return num1 
    elif num2 > num1:
        return num2 
    elif num1 == num2:
        return num1 
    else:
        return "Invalid"
    
result = find_largest(10,20)
print(result)




# Question - 30
# Write a function to determine if a person can enter a club.

def can_enter_club(age):
    if age >= 21:
        return True 
    else:
        return False 

result = can_enter_club(34)
print(result)



# Question - 31 
# Python Program to find Armstrong Number in an Interval 


# 10 to 100  -- first get the number ---- and then get all the digits, and based on the length, get the sum of that power of length, and if euqual to original number...then this is an armstrog number..print it

'''

Where is the probelem in this below code - 

'''

lower = int(input("Enter a Lower Range Value : "))
higher = int(input("Enter a Higher Range Value : "))

for num in range(lower,higher+1):  # 10,11,12,13.....20
   # print(num)
   temp = num
   armstrong = 0
   while num > 0:
      length = len(str(num))  # 2
      last = num % 10 
      armstrong = armstrong + last ** length 
      num = num // 10
   if temp == armstrong:
      print(num)
      




# Important Concept 
print(2%10)  # 2     
print(2/10)  # 0.2
print(2//10) # 0





"""
Working Fine 
"""
lower = int(input("Enter a Lower Range Value : "))
higher = int(input("Enter a Higher Range Value : "))

for num in range(lower,higher+1):  # 10,11,12,13.....20
   # print(num)
   length = len(str(num))  # 2  [this line I did mistake...find length earlier]
   temp = num
   armstrong = 0
   while num > 0:
      last = num % 10 
      armstrong = armstrong + last ** length 
      num = num // 10
   if temp == armstrong:
      print(temp)
      






# prime number without modulo operator in python
# fibonacci series 

# How we will get to know that...I need to declare a variable outside the loop or inside the loop. 







# Question - 32

# Python Program to find the sum of natural numbers 

n = int(input("Enter the number till which you want the sum of natural numbers : "))
sum = 0
for num in range(1,n+1):
   sum = sum + num 
print(sum)




# Question - 33 
# Python Program to display powers of 2 Using Anonymous Function 

# Anonymous Function is same as Lambda Function. Whenever you need to create a temporary function, use anonymous function. Take less lines of code.


power = lambda pow: 2**pow 
print(power(5))
   
   
# for all nterms 
nterm = int(input('Enter the number of terms : '))
result = list(map(lambda num : 2 ** num, range(1, nterm+1)))
print(result)
for n in range(1,nterm+1):
   print(f"The value of 2 raised to power {n} is {result[n-1]}")
   
   
   

# Question - 34
# Python Program to Find Numbers Divisible By Another Number 

# Using For Loop & Conditional Statements 

print("The Numbers divisible by 13 are in the range of 1 to 100 : ")
for num in range(1,101):
   if num % 13 == 0:
      print(num, end=" ", sep =" ")
      
      
# Using Lambda Function & Filter Function 

list1 = [12,23,43,26, 89, 39, 52, 13]
result = list(filter(lambda num : num % 13 == 0, list1))   # num will be takne from list, and that will be filter, then store in list 
print(f"The numbers that are divisible by 13 are {result}")




# Question - 35 
# Python program to convert decimal to binary, octal and hexadeximal 

# decimal - base is 10 - 0 to 9
# binary - base is 2 -  0 & 1   -- prefix is 0b
# octal - base is 8   --- prefix is 0o
# hexadecimal - base is 16   -- prefix is 0x

# Using Build in Function 
  
decimal = int(input("Enter a decimal number : "))
binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)
print(binary, octal, hexadecimal)
