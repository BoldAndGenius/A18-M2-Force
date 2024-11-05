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


number = input("Enter a Number : ")
ans = ""
for num in number:
    if num == "1":
        # print("One", end=" ")
        ans = ans + 'One '
    elif num == "2":
        ans = ans + 'Two '
    elif num == "3":
        ans = ans + 'Three '
    elif num == "4":
        ans = ans + 'Four '
    elif num == "5":
        ans = ans + 'Five '
    elif num == "6":
        ans = ans + 'Six '
    elif num == "7":
        ans = ans + 'Seven '
    elif num == "8":
        ans = ans + 'Eight '
    elif num == "9":
        ans = ans + 'Nine '
    elif num== "0":
        ans = ans + 'Zero '
print(ans)











# not working --- 0 is missed
given_number = int(input("Enter Any Number : "))
reverse = str(given_number)[::-1]
final = int(reverse)
ans = ''
while final > 0:
    last = final % 10  
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
    final = final // 10
print(ans)




# This below logic will not give the desired ouput...it will hide the 0 --- so use the above logic of string slicing

number = input("Enter a Number : ")  # 123
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
        
        
        
        
        
        
'''
Question Number 90 

Write a program to check weather the given tuple is palindrome or not

'''

given_tuple = (1,2,1)
reverse = given_tuple[::-1]
if given_tuple == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
    
    




'''
Question Number 89

 Q89.Write a program to check the type of data entered by the users
'''


data = eval(input("Enter any value : "))
if type(data) == int:
    print("Integer Data Type.")
elif type(data) == float:
    print("Float Data Type.")
elif type(data) == complex:
    print("Complex Data Type.")
elif type(data) == bool:
    print("Boolean Data Type.")
elif type(data) == list:
    print("List Data Type.")
elif type(data) == tuple:
    print("Tuple Data Type.")
elif type(data) == set:
    print("Set Data Type.")
elif type(data) == dict:
    print("Dictionary Data Type.")
elif type(data) == str:
    print("String Data Type.")
else:
    print("Invalid")
    
    



'''

Question Number 88 

Q88.Write a program to count number of consonants in the given string

'''
count = 0
given_string = "kiran"
for char in given_string:
    if char not in 'aeiouAEIOU':
        count = count + 1
print(count)








'''

Question Number 87 

.Write a program to find the length of the longest word

'''






'''
Question Number 86

Q86.Write a program to count number of words in the given string

'''

word = "kiran kumar"
number = 0 
for char in word:
    number = number + 1
print(f"The Number of Words in {word} is {number}")






'''
Question Number 56 

Q56.write a program to count the number of vowels present in a given string

'''

string = "kiran"
number = 0
for char in string:
    if char in "aeiouAEIOU":
        number = number + 1 
        
print(f"The Number of Vowels in {string} is {number}")




'''
Question Number 39

Write a program to print all the factors of a number using while loop.

'''
number = int(input("Enter a Number : "))
start = 1
while start <= number:
    if number % start == 0:
        print(start)
    start = start + 1
    
    
    

'''
Question Number 41

.Write a program to extract all the uppercase character from the given string

'''
given_string = "IAmAnAlphaMale"
for char in given_string:
    if char.isupper():
            print(char, end="  ")




'''

Question Number 42

 Q42.Write a Program to separate positive and negative number from a list.
'''

given_list = [1, 3.0, -1.2, True]
positive_number = []
negative_number = []
for item in given_list:
    if item > 0:
        positive_number.append(item)
    elif item < 0:
        negative_number.append(item)
    else:
        print("Invalid")
print(positive_number)
print(negative_number)



'''
Question Number 44 

Q44.Write a program to fetch only even values from a dictionary.

'''

dictionary = {'age1':21, "age2": 23, "rollno1":12, 'rollno2':28}

for keys in dictionary:
    if dictionary[keys] % 2 == 0:
        print(dictionary[keys])
        
        
        
        


'''
Question Number 45 

Write a program to extract all the string data items from the given list only if string is
 palindrome
 
 '''
 
list = ["kiran", "kumar", "maa", 'maam', 'dad', '1232', '12321']
for item in list:
    if type(item) == str  and item == item[ : : -1]:  # beautiful line
        print(item)
 
 
 

'''
Question Number 46

Write a program to extract all the special characters from the given string
'''

given_string = 'kiran is a good boy.@'
for char in given_string:
    if not (char.isalnum()):
        print(char)
        
        
    

'''

Question Number 47 

 Q47.Write a program to extract all the uppercase character,lower case character,numbers and
 special characters into four different output variables from the given string
 
 '''
given_string = "iIkIR#$123"
upper = ""
lower = ""
numbers = ""
special = ""
for char in given_string:
    if char.isupper():
        upper = upper + char 
    elif char.islower():
        lower = lower + char 
    elif char.isnumeric():
        numbers = numbers + char 
    elif not char.isalnum():
        special = special + char 
print(upper)
print(lower)
print(numbers)
print(special)



'''
Question Number 49 

.Write a program to convert all the lower case charater to uppercase characters present in
 a given string
 
'''

given_string = "Kiran"
lower_to_upper = given_string.upper()
print(lower_to_upper)






'''

Question Number 73


 Q73.Write a program to find the length of collection without using len function
 
'''

collection = [1,2,3]
length = 0
for item in collection:
    length = length + 1
print(f"The Length of {collection} is {length}")




'''
Question Number 72

Write a program to remove duplicate value from collection without converting to set

'''

# Using Set 

collection = [1,1,1,1]
unique = set(collection)
listt = list(unique)
print(listt)


# Using Loops 
# Revise it..............! 

collection = [1,1,1,2]
unique_collection = []
for item in collection:
    if item not in unique_collection:
        unique_collection.append(item)
print(unique_collection)





'''

Question Number 55 

Q55.Write a program to get the following output
 input=‘hai hello’
 output=’olleh iah’
 
'''
input= 'hai hello'
output = input[::-1]
print(output)




'''
Q58.Write a program to get the following output
 input=[‘jiocinema.com’ , ’file.py’ , ‘web.html’]
 output=[‘com’ , ’py’ , ‘html’]
'''


input=['jiocinema.com' , 'file.py' , 'web.html']
output = []
for item in input: 
    final = item.split('.')[-1]
    output.append(final)
print(output)




input = ['kiran kumar', 'pawandeep kaur']
for item in input:
    final = item.split()[-1]
    print(final)
    
    
    
    

'''
Question Number 37 

Q37.Write a Program to print all the characters in the string ‘PYTHON’ using while loop.

'''

string = 'PYTHON'
for char in string:
    print(char)
    
    
    
    
'''
Question Number 22

 Q22. Write a program to convert Decimal to Binary.
 
'''

decimal_value = int(input("Enter any decimal value : "))
binary_value = bin(decimal_value)
print(binary_value)






'''
Question Number 23

 23. Write a program to convert Binary to Decimal.
 
'''

binary_value = input("Enter any Value: ") 
decimal_value = int(binary_value,2)
print(decimal_value)

# int(binary_str, 2) to convert the binary string to a decimal integer.




'''
Question Number 24

Write a program to check whether a number is palindrome or not.

'''

number = int(input("Enter Any Number : "))
temp = number
reverse = 0
while number > 0:
    last = number % 10 
    reverse = reverse * 10 + last
    number = number // 10 
if temp == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
    
    
    
    
    
'''

Question Number 26

 Q26. Write a program to accept 10 numbers from the user and display it’s average
 
 '''


count = 1
sum = 0
while count <= 10:
    number = int(input("Enter Numbers : "))
    sum = sum + number
    average = sum / 10 
    count = count + 1
print(average)
 
 
 
 
 
 
'''
Question Number 27

 Q27. Write a program to accept 10 numbers from the user and display the largest & smallest
 number number.

'''
 
 
 
count = 1
largest = 0 # give the smallest value
smallest = 100000 # give the largest value
while count <= 5:
    number = int(input("Enter Numbers : "))
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
    # average = sum / 10 
    count = count + 1
print(largest)
print(smallest)



# Logic 2 

list_number = []

# print("Enter 10 Numbers.")
for num in range(1,11):
    numbers = int(input("Enter a number: "))
    list_number.append(numbers)

print(max(list_number))
print(min(list_number))







'''

Question Number 19 

 Q19. Write a program to enter the numbers till the user wants and at the end it should display
 the sum of all the numbers entered.
 
 '''
 
 
sum = 0
while True:
    number = input("Enter a Number  (or type done to finish): ")
    
    if number.lower() == "done":
        break 
    
    sum = sum + int(number)
print(sum)







'''
Question Number 20 

 Q20. Write a program to enter the numbers till the user enter ZERO and at the end it should
 display the count of positive and negative numbers entered.
'''

count_positive = 0
count_negative = 0
while True:
    number = int(input("Enter numbers or (enter zero)"))
    if number>0:
        count_positive = count_positive + 1
    elif number < 0:
        count_negative = count_negative + 1
    if number == 0:
        break
print(f"Positive Numbers Count : {count_positive} and Negative Numbers Count : {count_negative}")





'''
Question Number 21
Q21. Write a program to find the HCF of two numbers entered from the user.
'''

num1 = int(input("Enter the Number 1 : "))
num2 = int(input("Enter the Number 2 : "))
if num1 < num2:
    for n in range(1,num1+1):
        if (num1 % n == 0) and (num2 % n == 0):
            hcf = num1 
else:
    for n in range(1,num2+1) :
        if (num2 % n == 0) and (num1 % n == 0):
            hcf = num2 
print(hcf)
            
# 8 12 -- 4


















'''

Question Number 30 

Q30.Write a program to print the following series till nterms.
 2,22,222,2222_____nterms
 
 [Revise Revise Revise Revise ]

'''


# first step is understand the pattern and the based on that, create logic 





first = "2"
for i in range(1,num+1):
    if i < num:
        print(first, end=" , ")
    else:
        print(first)

    first = first + "2"






# Failed

# num = 10


# n = "2" 
# print(int(n)) # 2
# for _ in range(1,num+1):
   
#     length = len(n) # 1
#     final = length + 1 # 2
#     n =  n * final # "2"*2 = '22'
#     print(n)


    
