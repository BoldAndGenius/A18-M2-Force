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


# Method - 2: Using Multiple Variable Creation

num1 = 10
num2 = 20
num1, num2 = num2,num1 
print(f"num1 -> {num1} and num2 -> {num2}")