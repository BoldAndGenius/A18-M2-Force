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