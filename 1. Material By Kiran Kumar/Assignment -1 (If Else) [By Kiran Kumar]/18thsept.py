## Daily Solve 10 Questions (It's a challenge to me!!! - Let's say who will win! )


# Question - 1
# Write a program to print the square of a given integer number.
  
num = int(input("Enter a number :"))
print("The square of a given number is : ", num*num)

# or
print(f"The square of a given number is : {num*num}")

# or
print("The square of a given number is", num**2)   # Using exponential operator





# Question - 2
# Write a program to find the product of two float numbers.

num1 = float(input("Enter a number 1 :"))
num2 = float(input("Enter a number 2 :"))
print("The product of num1 & num2 is :", num1 * num2)

# or
print(f"The product of {num1} & {num2} is {num1*num2}")





# Question - 3
# Write a program to find the area of a rectangle.

length = float(input("Enter a length :"))
width = float(input("Enter a breadth :"))
print("The area of rectange is :",length*width)
#or
print(f"The area of rectange is : {length*width}")





# Question - 4
# Write a program to reverse the given string.

my_string = input("Enter a string :")
reverse = my_string[ : : -1]  
# start = 0, end = (length of a string - 1), step = -1
# As step is negative, therefore the start become end and end become start.
# So, start = -1, end = -len, and step = -1, 
# It means, it will move from -1st index to -length. 
# reverse = my_string[ : : -1]   This is same as -->  my_string[-1  :  -(len(my_string)+1):  -1]
# my_string[ : : 1]  is same as --- >  my_string [ 0 : len(my_string)  : 1]
# print(my_string [ 0 : len(my_string)  : 1])

print("The reversed string is :", reverse)


# print(my_string[1:3])





# Question - 5 
# Write a Program to find the sum, difference, product and division.Between 2 integer numbers.


num1 = int(input("Enter a number 1 :"))
num2 = int(input("Enter a number 2 :"))
print("The sum is :",num1+num2)
print("The difference is :",num1-num2)
print("The product is :",num1*num2)
print("The division is :",num1/num2)  # Gives the float values




# Question - 6 :
# Write a program to find the simple interest.


Principal = float(input("Enter Principal Amount :"))
Interest = float(input("Enter the Rate of Interest :"))
Time = float(input("Enter the Time Period in Years :"))
print("The Simple Interest is :", (Principal * Interest * Time)/100 )


# Question - 7 :
# Write a program to calculate area of triangle.

Base = float(input("Enter the Base :"))
Height = float(input("Enter the Height :"))
print("The Area of Triange is :", (Base*Height)/2)


# Question - 8 :
# Write a Python code to swap two variables. 
# Use temporary variable

num1 = int(input("Enter a number 1 :"))  # 5
num2 = int(input("Enter a number 2 :"))  # 10
print("Before Swapping :", num1, num2)
temp = num1  # temp = 5
num1 = num2  # num1 = 10
num2 = temp  # num2 = 5
print("After Swapping :",num1, num2)


# Logic - 2 :  Using Multivalue Assignments 

num1 = int(input("Enter a number 1 :"))
num2 = int(input("Enter a number 2 :"))
print(f"Before Swapping : num1 = {num1} and num2 = {num2}")
num1, num2 = num2, num1   #This is the main logic of this question
print(f"After Swapping : num1 = {num1} and num2 = {num2}")





# Question - 9 :
# Write a Python program to calculate the square root of a given number.


# number = int(input("Enter a number :"))
# print("The square root of a number is :",sqrt(number))   --This is wrong.
# (Error )


import math
number = float(input("Enter a number :"))
sqrt = math.sqrt(number)
print(f"The Square root of {number} is {sqrt}")





# Question - 10 :
# Write a Python program to find the area of a circle.

radius =float(input("Enter the radius :"))
pie = 3.14
print("Area of a circle is :", pie*radius*radius)

# Method - 2  : Using math module  (More Precise)

import math
radius = float(input("Enter the radius :"))
area = math.pi *radius *radius     # math.pi provides the value of π from the math module. 
print(f"The Area of Circle is : {area}")


