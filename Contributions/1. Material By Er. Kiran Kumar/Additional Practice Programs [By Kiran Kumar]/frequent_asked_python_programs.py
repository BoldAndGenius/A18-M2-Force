
# Frequently Asked Python Program 

"""

# Question Number - Swap 2 Numbers 

"""

# Approach -1 
# By Using Temporary Variable 

num1 = 10 
num2 = 20 
print("Before Swapping",num1, num2)

temp = num1 
num1 = num2 
num2 = temp 

print("After Swapping",num1, num2)


# Approach - 2
# Without Temporary Variable 

num1 = 10 
num2 = 20 
print("Before Swapping",num1, num2)

num1,num2 = num2,num1 

print("After Swapping",num1, num2)






# practice
# To swap two numbers, there is 2 approach..
# With using temporary variable 

num1 = 10
num2 = 20
print(num1,num2)
temp = num1 
num1 = num2 
num2 = temp 
print(num1,num2)


# Without Using Temprary Variable 
num1 = 10 
num2 = 20 
print(num1,num2)
num1, num2 = num2,num1 
print(num1,num2)













'''
Question - 2 
Check Number is Prime or Not 


What is Prime Number.
Natural Number > 1
Which has only 2 Factors 1 and itself. 

eg -

19 => 1 and 19 => Prime Number.
28 => 1,2,4,7,14,28 => Not a Prime Number.
'''

number = int(input("Enter a Number : "))
prime = True 
for num in range(2,number):
    if number%num == 0:
        prime = False 
if prime == True:
    print("Prime Number")
else:
    print("Not a Prime Number")
    
    
    
    
# Practice 
number = int(input("Enter a Number : "))
prime = True 
for num in range(2,number):
    if number % num == 0:
        prime = False 
if prime == True:
    print("Prime Number")
else:
    print("Not a Prime Number.")
    
    


number = int(input("Enter a Number : "))
prime = True 

for num in range(2,number):
    if number % num == 0:
        prime = False 
if prime == True:
    print("Prime Number.")
else:
    print("Not a Prime Number.")


'''
2nd Approach 

What is Prime Number.
Natural Number > 1
Which has only 2 Factors 1 and itself. 

eg -

19 => 1 and 19 => Prime Number.
28 => 1,2,4,7,14,28 => Not a Prime Number.
'''

num = int(input("Enter a Number : "))
count = 0
if num > 1:
    for n in range(1,num+1):
        if num % n == 0:
            count = count + 1
    if count == 2:
        print("Prime Number.")
    else:
        print("Not a Prime Number.")








'''
Question - 3
How to find Factorial of a Number.
'''



# Approach 1 = Using Looping Statements  (Iterative Approach)

number = int(input("Enter a Number : "))  # 5! 
factorial = 1 
if number == 0:
    factorial = 1 
elif number == 1:
    factorial = 1 
elif number > 1:
    for num in range(1,number+1):
        factorial = factorial * num 
elif number < 0:
    print("Factorial doesn't exist for Negative Number.")
else:
    print("Invalid")
print(f"The Factorial of {number} is {factorial}")







factorial = 1
num = int(input("Enter a Number : "))

if num < 0:
    print("Factorial of a Negative Number doesn't exist.")
elif num ==0:
    print("The Factorial of 0 is 1.")
else:
    for i in range(1,num+1):
        factorial = factorial * i 
    print(f"The Factorial of {num} is {factorial}")





# Approach 2 = Using Recursion   [Recursive Approach]

# function calling the same function inside the same function is a recursive function.

def factorial(num):
    if num == 0 or num == 1:
        return 1 
    else:
        return num * factorial(num-1)
print(factorial(5))


# Using Ternary Operator 

def factorial(num):
    
    # return 1 if (num==0 or num ==1) else return n*factorial(n-1)     -- no need of return after else 
    return 1 if (num==0 or num ==1) else  num * factorial(num-1)
print(factorial(5))


# Using Ternary Operator --- practice 

def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num-1)
print(factorial(7))


def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num-1)             
# there is no need of return for the else block, just write the else, and write the statements 
print(factorial(5))


def factorial(num):
    return 1 if num == 0 or num ==1 else num * factorial(num-1)
print(factorial(5))


# Failure 
def factorial(num,start=1):
    if num == start:
        return None
    elif num == 0 or num == 1:
        return 1 
    else:
        return factorial(num)*factorial(num-1)
print(factorial(5))







# Practice -


def factorial(num):
    if num == 0 or num == 1:
        return 1 
    else:
        return num * factorial(num-1)
print(factorial(5))

def factorial(num):
    if num == 0 or num == 1:
        return 1 
    else:
        return num * factorial(num-1)
print(factorial(5))



def factorial(num):
    if num == 0 or num == 1:
        return 1 
    else:
        return num *factorial(num-1)
print(factorial(5))


def factorial(num):
    if num == 0 or num == 1:
        return 1 
    else:
        return num * factorial(num-1) 
print(factorial(10))


# A function which is calling the same function is called Recursive Function.

def factorial(num):
    if num == 0 or num == 1:
        return 1 
    else:
        return num * factorial(num-1)
print(factorial(6))


# Write a recursive function for factorial program

def factorial(num):
    if num == 0 or num == 1:
        return 1 
    else:
        return num * factorial(num-1)
print(factorial(4))




# Factorial using Loops 

number = int(input("Enter a Number : "))
factorial = 1
if number < 0:
    print("Factorial of a Negative Number not possible.")
elif number == 0:
    print("The Factorial of 0 is 1.")
else: 
    for num in range(1,number+1):
        factorial = factorial * num
print(f"The Factorial of {number} is {factorial}")



# Factorial using Loops 

number = int(input("Enter a Number :"))
factorial = 1
if number < 0:
    print("Factorial of a Negative Number not possible. ")
elif number == 0:
    print("The Factorial of 0 is 1.")
else:
    for num in range(1,number+1):
        factorial = factorial * num 
print(f"The Factorial of {number} is {factorial}")


# Factorial using recursion 

def factorial(num):
    if num == 0 or num == 1:
        return 1 
    else:
        return num * factorial(num - 1)
print(factorial(7))