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