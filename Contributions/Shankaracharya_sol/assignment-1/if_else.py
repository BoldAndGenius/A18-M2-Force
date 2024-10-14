#Uni whether the first value present inside the given list is complex or not.
list_ = eval(input("Enter a list:"))
first_value = list_[0]
data_type = type(first_value)
if data_type == complex:
    print("yes,the first value of the list is complex")
else:
    print("The first value of the list is not complex")

#Write a program to take and consider a tuple collection consisting of only two values. Check whether the taken tuple is homogeneous or heterogeneous.
tuple_ = eval(input("Enter a tuple consisting of two values:"))
first_value = tuple_[0]
second_value = tuple_[1]
data_type_first= type(first_value)
data_type_second = type(second_value)
if data_type_first == data_type_second:
    print("It is homogeneous")
else:
    print("It is heterogenous")
    
#Write a program to check whether the given integer number is multiple of 10 or not.
num = int(input("Enter a number:"))
if num % 10 == 0:
    print("number is multile of 10")
else:
    print("num is not multiple of 10")

#Write a program to consider an integer number. If the number is even then print square of the number else print the cube of the number.
num = int(input("Enter an integer:"))
if num % 2 == 0:
    square = num ** 2
    print(f"{square} is the square of {num}")
else:
    cube = num ** 3
    print(f"{cube} is the cube of {num}")

#Write a program to check whether the given string is palindrome or not.
string = input("Enter a string:")
new_string = string[::-1]
if new_string == string:
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palidrome")
    
#Write a program to consider string input, if it is having more than three characters then print length of the string else print string as it is.
string = input("Enter a string:")
if len(string) > 3:
    print(len(string))
else:
    print(string)
    
#Write a program to check whether the user is eligible to vote or not.
age = int(input("Enter your age:"))
if age > 18:
    print("You are eligible to vote")
else:
    print("you are not eligible for vote")

#Write a program to check whether a number is divisible by 7 or not.
num = int(input("Enter a number:"))
if num % 7 == 0:
    print(f"{num} is divisble by 7")
else:
    print(f"{num} is not divisble by 7")
    
#Write a program to check whether the last digit of a number entered by the user is divisible by three or not.
num = input("Enter a number:")
new_num = int(num[-1])
if new_num % 3 == 0:
    print("it is divisble by 3")
else:
    print("it is not divisble by 3")
    
#Write a program to check whether the year is leap year or not.
year = int(input("Enter a year in YYYY format:"))
if year % 4 == 0 or year % 400 == 0:
    print("it is a leap year")
else:
    print("it is not a leap year")
    
#Write a program to check whether a number entered is a 3 digit number or not.
num = input("Enter a number:")
if len(num) == 3:
    print("it is 3-digit number")
else:
    print("It is not a 3-digit number")
    
#Write a program to find the largest number out of two numbers expected from the user.
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
if num1 > num2:
    print(f"{num1} is greater")
else:
    print(f"{num2} is greater")
    
#Write a program to check whether a number.Entered by the user is positive or negative.
num = int(input("Enter num:"))
if num >= 0:
    print(f"{num} is positive")
else:
    print(f"{num} is negative")
    
#Write a program.To check whether a number accepted from the user is divisible by two and three both.
num=int(input("Enter a number:"))
if num % 2 == 0 and num % 3 == 0:
    print("it is divisible by 2 and 3 both.")
else:
    print("It is not divisible by 2 and 3 both.")'''
