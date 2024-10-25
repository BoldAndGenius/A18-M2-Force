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