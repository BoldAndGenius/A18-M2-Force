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










# Write a function to print the length of a list (list is the parameter).

def length_of_list(mylist):
    return len(mylist)

mylist = [1,2,3,"Kiran", True]
length = length_of_list(mylist)
print(f"The Length of {mylist} is {length}")

'''
Output -
The Length of [1, 2, 3, 'Kiran', True] is 5
'''



# Second Approach
cities = ["Bombay", "Bangalore", "Kolkata", "Dubai", "Delhi"]
heroes = ["Thor", "Ironman", "Captain America", "Shaktiman"]
def print_len(list):
    print(len(list))
    
print_len(cities)
print_len(heroes)





'''
Write a Function to print the elements of a list in a single line (list is the parameter).
'''

def list_elements(mylist):
    for item in mylist:
        print(item, end=" ")

mylist = [10,20,30,40,50]
list_elements(mylist)


'''
Output -

10 20 30 40 50

'''








'''
Write a function to find the factorial of n. (n is the parameter).

'''


# Method - 1 : Using Math Module

def find_factorial(n):
    import math
    return math.factorial(n)
n = int(input("Enter Any Number : "))
factorial = find_factorial(n)
print(f"The Factorial of {n} is {factorial}")


# Method - 2 : Using For Loop

def find_factorial(n):
    fact = 1
    for num in range(1,n+1):
        fact = fact * num
    return fact
n = int(input("Enter Any Number : ")) # 5
factorial = find_factorial(n)
print(f"The Factorial of {n} is {factorial}")








'''
Write a function to convert USD to INR.

'''

# 1 USD = 83 INR

def usd_to_inr(usd):
    return usd*83

usd = 10
conversion = usd_to_inr(usd)
print(f"USD Amount = {usd} $ and INR Amount after conversion is = {conversion} Rs.")


'''
Output -

USD Amount = 10 $ and INR Amount after conversion is = 830 Rs.

'''

# This is what we need to do in Functions 
# input kya aaiga hai, kaam kya karna hai, and ouput kya aa jaiga


'''
Write a function for a number n, If n is odd, print ODD and if n is Even, print EVEN.

'''

def odd_or_even(n):
    if n%2 == 0:
        print("Even Number.")
    else:
        print("Odd Number.")
n = int(input("Enter anu number : "))
odd_or_even(n)













'''
Recursion -

When a function calls itself repeatedly. 

Loops ka hi ek khatarnak version hai Recursion. Most of the cases, we may don't even require a Recursion. But for few specific cases, If we write same code in Loop, it become complicated, but with Recursion it become easy. 

Generally, for easy stuff we prefer to use Loops. 

All the tasks that we do with the help of loops, that can be done using Recursion as well. 
And all the tasks that can be done with the help of recursion, that can also be done using Loop. 

So, Loops and Recursion are interrelated. 
Same kaam ham dono se hi kar sakte hai. For few case, we prefer to use loop. and fir baad me agr ham DSA sikhne nikle hai, to kuch ese case niklenge jaha recursion hame simple code dega as compare to loops. 


'''


# return     - if we don't pass any value, we are returning control. as such as not returning any value. 
# can't call the function infinite times, we have to give one condition based on that we can return it. This condition is called base case. Base on that we return it. 

# Jese loop ke andar stopping condition hoti hai, while condition:  this condition will decide ki loop chalna chahiye ki nahi...Vese hi recursion ke andar base case hota hai...jo decide karta hai..ki yaha pe recursion roak jana chahiye ya nahi rukna chahiye....this is called base case. Recursion kab ruke...jab n ki value 0 ho jai. 

# Understand Recursion, Understand the Call Stack, it gonna help you when you learn any complex thing in Python.

# If we remove the base case, jese loop infinitel run kar jata tha..to yaha recursion infinitely chal jaiga...and at a point jab puri memory ko occupy kar legi.. and your code gets crashed.  --   
# RecursionError --- maximum recursion depth exceeded while calling a Python. ....so that's why base case is important in Recursion. 

# Recursion ke andar ham kese recursive code ko likhte hai...ham apna kaam dekhte hai ki mujhe kaam kya karvana hai...uske baad mera base case kya hona chahiye...

# General case me ham recursion ko use nahi karte hai....recursion kuch specific case me hi ham use karte hai. 
# General case me ham loop hi use karte hai. 





'''
Print n Natural Number Using Recursion. 

'''

# Recursive Function
def n_natural_number(n):
    if n == 0:  # Base case
        return
    print(n)
    n_natural_number(n-1)
    
n = int(input("Enter a Number: ")) # 5
n_natural_number(n)




# Jaha recurrence relation banta hai, vaha recursion likha ja sakta hai. 
# recurrence matlab -- esi cheeze jo reoccur kar rahi hai. Jo dubara repeat hokar aa rahi hai. --- bari cheez ka chota version...it means recurrence...hence recursion we can use here. 
# Example - Factorial of a number 




'''
Write a program to find the Factorial of Number using Recursion.

'''



def find_factorial(n):
    if n==0 or n==1 :
        return 1 
    return n * find_factorial(n-1)

n = int(input("Enter Any Number : "))
factorial = find_factorial(n)
print(f"The Factorial of a {n} is {factorial}")










'''
Write a recursive function to calculate the sum of first n natural numbers.
'''

def sum_of_n_natural_numbers(n):
    if n==1:
        return 1
    return n + sum_of_n_natural_numbers(n-1)
    
n = int(input("Enter a Number : "))  # 5
sum = sum_of_n_natural_numbers(n) 
print(f"The Sum of {n} Natural Number is {sum}")







'''
Write a Recursive Function to print all elements in a list. 
Hint: Use list & index as parameters.

'''
def print_elements_of_list(list,index=0): # recursive function
    if index == len(list):   # base condition
        return
    print(list[index])
    return print_elements_of_list(list, index+1)  # updaing the index 

list = eval(input("Enter any list : "))  # [10,20,30]
print_elements_of_list(list)



