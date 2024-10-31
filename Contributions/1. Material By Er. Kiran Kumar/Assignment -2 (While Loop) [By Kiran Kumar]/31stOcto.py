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




'''
Question Number - 8

Write a program to print table of a number entered from the user.

'''

number = int(input("Enter a number for which you want to print the table : "))
start = 1
while start <= 10:
    print(f"{number} X {start} = {number*start}")
    start = start + 1
    
    


'''
Question Number - 9

Write a program to print all even numbers that falls between two numbers (exclusive both
 numbers) entered from the user using while loop.

'''

lower = int(input("Enter lower value : "))
temp = lower
higher = int(input("Enter higher value : "))
while lower < higher:
    if lower % 2 == 0 and lower != temp:
        print(lower)
    lower = lower + 1



'''
Question Number - 10

 Write a program to check whether a number is prime or not using while loop.
 
'''

number = int(input("Enter a Number : "))  # 5
prime = True
start = 2
while start < number:
    if number % start == 0:
        prime = False 
        break 
    start = start + 1 
if prime == True:
    print("Prime Number ")
else:
    print("Not a Prime Number")
        





'''

Question Number - 11

Q11. Write a program to find the sum of the digits of a number accepted from the user.

'''

number = int(input("Enter a Number : "))  # 123
temp = number
sum = 0

while number > 0:
    last = number % 10
    sum = sum + last
    number = number // 10 
print(f"The Sum of {temp} is {sum}")
    
    


'''

Question Number - 12

Q12. Write a program to find the product of the digits of a number accepted from the user.

'''

number = int(input("Enter a Number : "))
temp = number
product = 1
while number > 0:
    last = number %  10
    product = product * last
    number = number // 10 
print(f"The Product of the digits of {temp} is {product}")





'''
Question Number - 13

 Q13. Write a program to reverse the number accepted from user using while loop

'''

number = int(input("Enter a Number : "))
temp = number 
reverse = 0
while number > 0:
    last = number % 10 
    reverse = reverse * 10 + last   # Revise this logic 
    number = number // 10
print(reverse)