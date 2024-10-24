
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
