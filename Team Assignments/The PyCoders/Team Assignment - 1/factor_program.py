# Factor Program - 1 : Find Factors of a Number num.

num = int(input("Enter a Number : "))
print("The Factors are : ", end=" ")
for divisor in range(1,num+1):
    if num % divisor == 0:
        print(divisor,end=" ")
    
'''
Input - 30

Output -

The Factors are :  1 2 3 5 6 10 15 30 

'''






# Factor Program - 2 : Find if a Number is a Prime Number or not.

# A Prime Number is a number that divisible by only 1 & itself. So, it have only two factors.
# 5  -- 5 is divisible by only 1 & 5. 


num = int(input("Enter a Number : "))
count = 0
for factor in range(2,num):
    if num % factor == 0:
        count = count + 1
if count == 0:
    print("Prime Number.")
else:
    print("Not a Prime Number.")
    
    
    



num = int(input("Enter a Number : "))
count = 0
for factor in range(1,num+1):
    if num % factor == 0:
        count = count + 1
if count == 2:
    print("Prime Number.")
else:
    print("Not a Prime Number.")
    
    
    
    
    
    
    
    
    
    
# Factor Program - 3 : Find if a Number is a Composite Number or not.

# Composite Number - Number which has more than two factors.  
# (excluding 1 & number itself)

num = int(input("Enter a Number : "))
count = 0
for divisor in range(1,num+1):
    if num % divisor == 0:
        count = count + 1
    
if count > 2:   # we need to discard 1 & number itself. 
    print("Composite Number.")
else:
    print("Not a Composite Number.")
    
    
    
    
    
    
    
    
    
    
# Factor Program - 4 : Find if a Number is a Perfect Number or not.
# Perfect Number - A Perfect Number is equal to to sum of its divisors or factors except itself.   Eg. 6 = 1 + 2 + 3 

num = int(input("Enter a Number : "))
count = 0
sum = 0
for divisor in range(1,num):
    if num % divisor == 0:
        sum = sum + divisor
    
if num == sum:
    print("Perfect Number.")
else:
    print("Not a Perfect Number.")
    
    
    
    

# Factor Program - 5 : Find if a Number is an Abundant Number or not.
# Abundant Number - Sum of factors is greater than the number itself.
# Eg. 12   - 1,2,3,4,6 = 16 > 12  (that number is excluding in factors)

num = int(input("Enter a Number : "))
sum = 0
for divisor in range(1,num):  # num is not considered
    if num % divisor == 0:
        sum = sum + divisor
if sum > num:
    print("Abundant Number.")
else:
    print("Not an Abundant Number.")
    
    
    
    
    

# Factor Program - 6 : Find if a Number is a Deficient Number or not.
# Deficient Number - Sum of factor is less than the number itself.
# Eg. 21 -- Factors = 1,3,7 = 11 <21   (that number is excluding)


num = int(input("Enter a Number : "))
for divisor in range(1,num):
    if num % divisor == 0:
        sum = sum + divisor
if num > sum:
    print("Deficient Number.")
else:
    print("Not a Deficent Number.")
    
    
    





# Factor Program - 7 : Find if a Number is a Pronic Number or not.
# Pronic Number - Pronic Number is the product of two consecutive integers. In the form,  n (n+1)    eg. -  56 = 7 * 8 

num = int(input("Enter a Number : "))
pronic = 0
for divisor in range(1,num+1):
    if num % divisor == 0:
        if ( divisor * (divisor + 1) ) == num:
            pronic = pronic + 1
if pronic == 0:
    print("Not a Pronic Number.")
else:
    print("Pronic Number.")
            