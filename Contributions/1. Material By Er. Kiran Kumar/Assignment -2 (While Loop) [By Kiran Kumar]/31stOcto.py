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
    
    
    
    
    
    
    
    
    
    
    
'''
Question Number - 2

Q2. Write a program to print first 10 integers and their squares using while loop.

'''

number = 1
while number <= 10:
    print(number,"   ", number ** 2)
    number = number + 1
    
    
    


'''
Question Number - 3

 Write while loop statement to print the following series: 10, 20, 30 … … 300
 
 [Revise Revise]
 
 '''
 
number = 10
while number <= 300:
    if number < 300:
        print(number, end=",")
    else:
        print(number)
    number = number + 10
    
    
    


'''
Question Number - 4

Write a while loop statement to print the following series 105, 98, 91 ………7.

'''

number = 105 
while number >= 7:
    if number > 7:
        print(number,end=",")
    else:
        print(number)
    number = number - 7
    
    


'''
Question Number - 5 

Write a program to print first 10 natural number in reverse order using while loop. 

'''

number = 10 
count = 1
while count <= 10:
    if count < 10:
        print(number,end=' , ')
    else:
        print(number)
    number = number - 1
    count = count + 1
    
    


'''
Question Number - 6 

Write a program to print sum of first 10 Natural numbers.
 
'''


number = 1
count = 1
sum = 0
while count <= 10:
    sum = sum + number
    number = number + 1
    count = count + 1
print("Sum of First 10 Natural Numbers : ",sum)




'''
Question Number - 7

Write a program to print sum of first 10 Even numbers.

'''


number = 0
count = 1
sum = 0
while count <= 10:
    sum = sum + number 
    count = count + 1
    number = number + 2
print("Sum of the first 10 even numbers:", sum)



