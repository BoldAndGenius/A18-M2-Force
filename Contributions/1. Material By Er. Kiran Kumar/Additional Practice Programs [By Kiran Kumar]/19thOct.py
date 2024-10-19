# Removing Code Redundancy using Functions  

num1 = 10
num2 = 30
sum = num1 + num2
print(sum)

# lines of code

num1 = 34
num2 = 120
sum = num1 + num2
print(sum)

# lines of code

num1 = 41
num2 = 120
sum = num1 + num2
print(sum)

# Only for addition logic, if we want the same logic at our codebase multiple times, then we have to use 4 lines of code again again. This is called Code Repetition or Code Redundancy. 

# Code Redundancy is a sign of bad programmer. 
# So, Use Functions to remove code redundancy from your program. 

# Removed the code redundancy using Functions

# function definition
def cal_sum(num1,num2):  # num1,num2 are called parameters
    print(num1+num2)

# function calling 
cal_sum(10,30)  # 10,20 are called arguments   # arguments ki value hamere parameter me store ho jati hai. 
cal_sum(34, 120)
cal_sum(41, 120)

'''
Output -
30
154
161
'''
# now using only 5 lines of code.
# Whenever you see any code redundancy or there is any repetition of code, create a function of it. It is a good practice.

# You can also return the values

def cal_sum(num1,num2):
    return num1+num2 
result1 = cal_sum(10,20)  # store the value in a variable
result2 = cal_sum(34, 120)
result3 = cal_sum(41, 120)
print(result1)
print(result2)
print(result3)

'''
Output -

30
154
161
'''














# Inside function we can use loop, if else. But it should be used with proper Indentation


# print() -- it is a pre defined function. It's a function call. 
# print("Hello World")  -- we pass the Hello World as an argument. That stores to print's definition.  
# In Python, Functions are of two types -
# 1. Built-in Function - It's logic is already written in Python. We just call it.   Eg.  type(), len(), print(), range()

# sep = when comma is used, it gives a space
# end = After executing that particular line, the curson goes to next line.
print("Hello World", "Kiran", sep="") # default=   end="\n" sept=" "

# 2. User Defined Function - Programmer write this function.





# Default Parameters 
# Assigning a default value to parameter, which is used when no argument is passed. 

def cal_product(num1 = 10, num2 = 30):  # assigned default value to parameter
    return num1 * num2
product = cal_product()
print(product)

'''
Output -

300

'''




def cal_product(num1 , num2 = 30):  # assigned default value to parameter
    return num1 * num2
product = cal_product(10)  # one argument we passed, and the second argument it takes from the assigned default value as a parameter at function definition 
print(product)




# Now it will give error 
def cal_product(num1 = 30 , num2):  # Non default arguments should come first, and then default arguments should come
    # always give default value from the last. 
    return num1 * num2
product = cal_product(10)  # one argument we passed, and the second argument it takes from the assigned default value as a parameter at function definition 
print(product)


