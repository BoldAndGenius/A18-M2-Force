'''

List Comprehensions

Question: Write a Python list comprehension that generates a list of all numbers between 1 and 100 that are divisible by both 3 and 5.
Bonus: Modify the comprehension to include only those numbers where the sum of their digits is greater than 5.



Create a Python list containing the numbers 1 to 5. Write a script to print the list in reverse order.


Given a string s = "Hello, World!", write a Python script to convert the string to all lowercase letters and then print it.


Write a Python script that takes a user's age as input and prints whether they are a child (age < 18), an adult (18 ≤ age < 65), or a senior (age ≥ 65).


Write a Python loop that prints the numbers from 1 to 10, but for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". If a number is a multiple of both 3 and 5, print "FizzBuzz".

'''




# Question - 1
# Exchange the values of two numbers with & without using a temporary variable 

# With Temporary Variable (Method - 1)

num1 = int(input("Enter a number 1 :"))
num2 = int(input("Enter a number 2 :"))
# color bucket example -- use this logic
temp = num1
num1 = num2
num2 = temp
print(f"The first number is {num1}")
print(f"The second number is {num2}")



# Without Temporary Variable (Method - 2)
# we can use Arithmetic Operation for that 
num1 = int(input("Enter a number 1 :"))  # num1 = 10
num2 = int(input("Enter a number 2 :"))  # num2 = 20

num1 = num1 + num2  # num1 = 30  -- this is used for swapping!

num2 = num1 - num2  # num2 = 30 - 20 = 10 
num1 = num1 - num2  # num1 = 30 - 10 = 20
# wow, swapping done! 

print(f"The first number is {num1}")
print(f"The second number is {num2}")





# Question - 2
# Calculate the average of numbers in a given list

# first take elements of a list as in input in the list -- use for loop [easy]



# Wrong Logic - First Try

# total_elements = int(input("Enter the number of elements you want to enter :"))   # 3
# list = []
# for i in range(total_elements):    # it will from 0 to total_elements -- hence, total elments get it   # 0 to 2 it will go  # 0 # 1 # 2
#     element = input("Enter an Element :")   # element = '10'  # element = '20' # element = '30'
#     list.append(element)   # list = ['10']  # list = ['10', '20']  # list = ['10', '20', '30']
# # print(list) - the user entered list got printed 
# sum_of_elements = sum(list)
# print(sum_of_elements)
# average = sum_of_elements / total_elements
# print(f"The Average of elements in a {list} is {average}")

# Why my logic was wrong is....because I was using sum function on the string elements. It means, I need to typecaste it into 



# Try 2

total_elements = int(input("Enter the number of elements you want to enter :"))
list1 = []
for i in range(total_elements):  
    element = int(input("Enter an Element :"))
    list1.append(element)
# print(list1) - for testing
sum_of_elements = sum(list1)
average = sum_of_elements / total_elements
print(f"The Average of Elements in a {list1} is {average} ")








# Questin - 3
# Reverse a number using String Method

# number = int(input("Enter a Number : "))
# to reverse a number, first I need to access each elements of a number 
# I can't do anything on number, since number is in integer format, therefore convert to string, then only we can use string methods over it.

number = input("Enter a Number : ")
# As we know, using string slicing, we can easily move cursor from start to end in reverse order
reverse = number[ : :-1]   # here start = end,  and end = start,  and -1 means it will move from back side.

print(f"The reverse of {number} is {reverse}")




# Question - 3 
# Python Program to Reverse a String

# Method -1 (Using String Method)
string = input("Enter a String :")  #  'kiran'
reverse = string[::-1]
print(f"Reverse of {string} is {reverse}")

# Method - 2 (Using For Loop)
string = input("Enter a String :")  #  'kiran'
reverse = ''
for char in range(len(string)-1, -1, -1):
    reverse = reverse + string[char]
print(f"The reverse of {string} is {reverse}")
    
    


