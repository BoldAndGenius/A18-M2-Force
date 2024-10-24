
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



