'''

Question Number 1 

1. Write a program to print the following using while loop
 a. First 10 Even numbers
 b. First 10 Odd numbers
 c. First 10 Natural numbers
 d. First 10 Whole numbers
 
 
'''

# Answer 1

# a. First 10 Even numbers

start = 0
end = 20
while start < 20  :
    if start % 2 == 0:
        print(start)
    start = start + 1
    
    
    
# Dynamic -- More Optimized Code 

count = 1

number = 0
while count <= 10:
    
    print(number)
    number = number + 2
    
    count = count + 1
    
    
    



#  b. First 10 Odd numbers 

count = 1
number = 1
while count <= 10:
    print(number)
    number = number + 2
    count = count + 1
    
    
    

#  c. First 10 Natural numbers

number = 1
while number <= 10:
    print(number)
    number = number + 1
    
    

#  d. First 10 Whole numbers 

number = 0
while number < 10:
    print(number)
    number = number + 1