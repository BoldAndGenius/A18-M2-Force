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

def cal_sum(num1,num2):
    print(num1+num2)

cal_sum(10,30)
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