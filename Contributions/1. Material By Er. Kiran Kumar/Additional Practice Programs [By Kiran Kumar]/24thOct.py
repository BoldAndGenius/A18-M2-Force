
# Factorial of a Number 

# Using For Loop 
n = int(input("Enter a number : "))
fact = 1
for num in range(1,n+1):
    fact = fact * num 
print(f"The Factorial of a {num} is {fact}")
    
    
# Using Recursion 

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)
num = int(input("Enter a Number: "))
result = factorial(num)
print(f"The Factorial of {num} is {result}")







# Starting to Ending Point using Recursion

def start_to_end(start=1,end=10):
    if start>end:
        return None 
    else:
        print(start)
        start_to_end(start+1)

start_to_end()



# Ending to Starting Point using Recursion 
def end_to_start(start=10,end=1):
    if start<end:
        return None 
    else:
        print(start)
        end_to_start(start-1)
end_to_start()



# Ending to Starting Point Using Recursion (With 2nd Logic)

def end_to_start(start=1, end=10):  
    if start>end:
        return None 
    else:
        end_to_start(start+1)
        print(start)
end_to_start()   



# Even Numbers from start to end Using Recursion 

def even_number(start,end):
    if start>end:
        return None 
    else:
        if start%2 == 0:
            print(start)
        even_number(start+1,end)
even_number(1,21)




# Odd Numbers from start to end Using Recursion

def odd_numbers(start,end):
    if start>end:
        return None 
    else:
        if start % 2 != 0:
            print(start)
        odd_numbers(start+1,end)
odd_numbers(10,23)




# Divisible By 3 from start to end Using Recursion 

def divisible_by_3(start,end):
    if start > end:
        return None 
    else:
        if start%3 == 0:
            print(start)
        divisible_by_3(start+1,end)
divisible_by_3(1,51)



# Divisible By 5 from start to end Using Recursion 

def divisible_by_5(start,end):
    if start>end:
        return None
    else:
        if start % 5 == 0:
            print(start)
        divisible_by_5(start+1,end)
divisible_by_5(21,145)








# Total Time to Execute, to Print 1 to 10 Using For Loop (Using Time Module)


from time import time 
start = time()
for num in range(1,11):
    print(num)
end = time()
print(end-start)
# 0.003301858901977539 Seconds


# Total Time to Execute, to Print 1 to 10 Using Recursion (Using Time Module)
from time import time 
start = time()
def count_up(start:int, end:int):
    if start>end:
        return None 
    else:
        print(start)
        count_up(start+1,end)       
count_up(1,10)
end = time()
print(end - start)





# Import code of different module/file to your current file 

# maths.py 
def factorial(num):
    fact = 1
    if num == 0 or num==1 :
        return fact
    else:
        for num in range(1,num+1):
            fact = fact * num 
        return fact 


# use.py 
from maths import factorial   # from maths.py file (module), import the factorial function 
print(factorial(10))





# Write a Function to calculate the Factorial of a Number 

# factorial -- it is a product of a descending number till 1.
# 0! = 1
# 1! = 1
# 2! = 2*1 = 2
# 3! = 3*2*1 = 6

def factorial(number:int):
    fact = 1
    if number==0 or number ==1 :
        return 1 
    else:
        for num in range(1,number+1):
            fact = fact * num
        return fact 
result = factorial(5)
print(result)



# Factorial using For Loop

n = int(input("Enter a Number : "))
factorial = 1
for num in range(1,n+1):
    factorial = factorial * num 
print(f"The Factorial of {n} is {factorial}")
    
    
    
# Factorial using While Loop

num = int(input("Enter a Number : "))  # num = 5
# 5 -  5*4*3*2*1
temp = num
fact = 1
while num != 0:
    fact = fact * num
    num = num - 1
print(f"The Factorial of {temp} is : {fact} ")



# Fibonacci Series 

# first = 0
# second = 1
# print(first)
# print(second)

# # 0, 1, 1, 2, 3, 5 

# n = int(input("Enter the number of terms: "))
# while next_digit > n:
#     first = second  # first  = 1
#     second = first + second   # second = 1 + 1
#     next_digit = first + second 
#     print(next_digit)




# Swap Two Numbers 

num1 = 20
num2 = 30

num1, num2 = num2,num1
print(f"num1 -> {num1}")
print(f"num2 -> {num2}")



# Palindrome String 

# Logic - 1 : Using String Slicig 
string = input("Enter a String : ")
reverse = string[::-1]
if string == reverse:
    print("Palindrome.")
else:
    print("Not a Palindrome.")
    


# Logic - 2: Using For Loop
string = input("Enter a String : ") # kiran
reverse = ""
for char in string:
    reverse = char + reverse  #'k'+'' = 'k'  # 'i'+'k' = 'ik'  # 'r'+'ik;
# print(reverse)  
if string == reverse:
    print("Palindrome.")
else:
    print("Not a Palindrome.")
    


# Logic - Using While Loop  

string = input("Enter a String : ") # k i r a n 
                                    # 0 1 2 3 4
reverse = " "
index = len(string) - 1
while index >= 0: 
    reverse = reverse + string[index]
    index = index - 1
if reverse == string:
    print("Palindrome.")
else:
    print("Not a Palindrome.")
