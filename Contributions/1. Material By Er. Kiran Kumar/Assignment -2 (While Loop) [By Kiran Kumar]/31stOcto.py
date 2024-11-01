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




'''
Question Number - 14

 Q14. Write a program to display the number names of the digits of a number entered by user,
 for example if the number is 231 then output should be Two Three One.
 
 Lovely Question -- REVISE IT 
 
'''

number = int(input("Enter a Number : "))  # 123
temp = number   
reverse = 0

while number > 0:
    last = number % 10   # 3
    reverse = reverse * 10 + last
    number = number // 10
    
print(reverse)

'''
231 goes to 132 
290 goes to 92    (why not zero)

'''

ans = ''
while reverse > 0:
    last = reverse % 10  
    if last == 1:
        # print("One", end=" ")
        ans = ans + 'One '
    elif last == 2:
        ans = ans + 'Two '
    elif last == 3:
        ans = ans + 'Three '
    elif last == 4:
        ans = ans + 'Four '
    elif last == 5:
        ans = ans + 'Five '
    elif last == 6:
        ans = ans + 'Six '
    elif last == 7:
        ans = ans + 'Seven '
    elif last == 8:
        ans = ans + 'Eight '
    elif last == 9:
        ans = ans + 'Nine '
    elif last == 0:
        ans = ans + 'Zero '
    reverse = reverse // 10
print(ans)
    
    
    


'''
Question Number - 16 

Write a program to print the factorial of a number accepted from user.

'''

# 0! = 1
# 1! = 1
# 2! = 1*2 
# 3! = 3*2*1 


number = int(input("Enter a Number : "))
if number == 0:
    print(1)
elif number == 1:
    print(1)
else:
    fact = 1
    start = 1
    while start <= number:
        fact = fact * start
        start = start + 1 
    print(fact)
    
    
    





'''
Question Number - 17

Write a program to check whether a number is Armstrong or not. (Armstrong number is a
 number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)
'''

number = int(input("Enter a Number : "))
temp = number
length = len(str(number))
arm = 0

while number > 0:
    last = number % 10 
    arm = arm + last ** length 
    number = number // 10 

if temp == arm:
    print("Armstrong Number.")
else:
    print("Not an Armstrong Number.")
    
    



'''

Question Number 97 

 Q97.Write a program to check weather the first and last value in the collection is float if yes add those 2 values
 
 '''
 
collection = [1.2, 23, True, 3.5]
if type(collection[0]) == float and type(collection[-1]) == float:
    sum = collection[0] + collection[-1]
    collection.append(sum)
    print(collection)
else:
    print("Please Enter First & Last Value to be Float Data Type.")






'''
Question Number 96 

Q96.Write a program to extract all the non default values from the list

'''
# default value  - 0, 0.0, False, 0j, "", [],(),set(),{}


list = [1,2,0, 0.0, True, 89, False, "",[1,2], [], set(), {"name":"kiran"}, {}, 567]

for element in list:
    if element not in [0,0.0, False, 0j, "",[],(),set(),{}]:
        print(element,end=" , ")
        
        
        
'''
Question Number 95 

Write a program to extract all integer data items from tuple

'''

tuple = (1,2,3,4,5, True, 3.4, [1,2,3], 3+8j, {12,3}, (12,3), {"name":"kiran"})
for element in tuple:
    if type(element) == int:
        print(element)
        
        
    
    


'''
Question Number 94 

Q94.Write a program to whether the entered username and password is correct or not if not correct print enter again.

'''

while True: 
    username = input("Enter your Username : ")
    password = int(input("Enter Your Password : "))
    if username == 'kiran' and password == 1234:
        print("Welcome")
        break
    else:
        print("Enter Again.")





'''

Question Number 93 

 Q93:Write a program to find length of collection without using len function
 
 '''
 
 
collection = [1,2,3,4,5]
count = 0
for item in collection:
    count = count + 1
print(f"The Length of {collection} is {count}")
    




'''
Question Number 92 

Write a program to return the positions of vowels present in the given string

'''


string = "aikiran"
index = 0
for char in string:
    if char in "aeiouAEIOU":
        print(index)
    index =index + 1
    
    
    
    



'''
Question Number 91

Write a program to check weather the given collection is having nested collection or not

'''

collection = [1,2, [1,2], (1,2), True, 'kiran',{123,1}]

for item in collection:
    if type(item) in [ dict, set, list, tuple]:   # may get error, because earlier you used list & tuple as a variable ....so above don't use data type as a variable name, get conflicts. 
        print("Nested Collection")