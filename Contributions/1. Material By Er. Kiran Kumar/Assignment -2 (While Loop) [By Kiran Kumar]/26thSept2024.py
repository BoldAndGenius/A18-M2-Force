# Question - 1
# Write a program to print the following using while loop -
# a. First 10 Even numbers

# Method -1 (Using For Loop)

for i in range(0,21,2):
    print(i)
    
    
for i in range(20):
    if i%2 == 0:
        print(i)
# Method -2 (Using While Loop)
# i = 0
# number = 0
# while number < 10:  # 0<10  # 1<10
#     if i%2 == 0:  
#         print(i)  # 0  
#         number = number + 1  # number = 1 # number =2
#     i = i + 1  # i = 1  # i = 2
    
    
        
    
        
# b. First 10 Odd numbers

for i in range(1,21,2):
    print(i)

for i in range(20):
    if i%2 != 0:
        print(i)


# c. First 10 Natural numbers

for i in range(1,11):   # since, start from 1, and go to 10
    print(i)
    
# d. First 10 Whole numbers

for i in range(10):
    print(i)
    
    
    
    
    
    
    
# Question - 2
# Write a program to print first 10 integers and their squares using while loop

for i in range(10):
    print(i**2)
    
    


# Question - 3
# Write while loop statement to print the following series: 10, 20, 30 … … 300

# Using While Loop

i = 10
while i <= 300:
    print(i)
    i = i + 10
    




# Using For Loop - Method -1 
number = 0
for i in range(100):   # nice jugad, actually range function here I am using for timepass, in reality I am using break to control my break
    number = number + 10   # 0+10 = 10,    10+10 = 20,   20 + 10
    if number > 300:
        break
    print(number)

# Using For Loop -- Method 2 (MOR OPTIMIZED *****)
for i in range(10, 301, 10):
    print(i)
    
    
    
    
    
# Pending Task -
# Tomorrow try all the above questions using While Loop!!! -- Then only you can learn the power of While Loop (****)