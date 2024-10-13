# if else

# Question 34 - 
# Write a program to check whether the given number is even or odd.

given_number = int(input("Enter a number :"))
if given_number % 2 == 0:
    print("It's an even number ")
else:
    print("It's an odd number ")
    
    
    
# Question - 35 
# Write a program to check whether the given data is mutable or immutable.
given_data = eval(input("Enter a data :"))
if type(given_data) in [list,set,dict]:
    print("The entered data is mutable")
else:
    print("The entered data is immutable")
    

# Question - 36 
# Write a program to check whether the given data is single value or collection.
given_data = eval(input("Enter a data :"))
if type(given_data) in [int,float,complex,bool]:
    print("It's a single value data type")
else:
    print("It's a collection")


# Question - 37 
# Write a program to check whether a given character is a special symbol or not.
given_character = input("Enter a character :")
if ('a' <= given_character <= "z")  or ('A'<given_character<= "Z") or ('0'<=given_character <='9'):
    print("Not a Special Symbol")
else:
    print("It's a special symbol")
    

# Question - 38 
# Write a program to check whether the given string is having the middle character or not.
given_string = input("Enter a string :")
if len(given_string) % 2 != 0:
    print("Given String have a middle character")
else:
    print("Given string don't have a middle character")
    

# Question - 39
# Write a program to check whether the given 2 variables are pointing to the same memory location or not.
num1 = eval(input("Enter a number 1 :"))
num2 = eval(input("Enter a number 2 :"))
if id(num1) == id(num2):
    print("The given two numbers are pointing to the same memory location")
else:
    print("The given two numbers are pointing to different memory location")




# Question - 40
# Write a program to check whether the first value present inside the given list is complex or not.

given_list = [23, True, 3+5j ]   # [3+10j, 23, False]
if type(given_list[0]) == complex:
    print("Complex")
else:
    print("Not Complex")





# Question - 41 
# Write a program to take and consider a tuple collection consisting of only two values. Check whether the taken tuple is homogeneous or heterogeneous.

# A tuple is considered homogeneous if all its elements are of the same data type, and heterogeneous if the elements are of different data types.

tup = eval(input("Enter a tuple of length 2 : "))
if len(tup) != 2:
    print("The lenght of tuple should be 2")
else:
    if type(tup[0]) == type(tup[1]):
        print("Homogenous Tuple.")
    else:
        print("Heterogenous Tuple.")
    




# Question - 42 
# Write a program to check whether the given integer number is multiple of 10 or not.
given_integer = int(input("Enter a number :"))
if given_integer % 10 == 0:
    print("The given integer is multiple of 10")
else:
    print("The given integer is not multiple of 10")



# Questtion - 43 
# Write a program to consider an integer number. If the number is even then print square of the number else print the cube of the number.

number = int(input("Enter an integer number :"))
if number % 2 == 0:
    print(number ** 2)
else:
    print(number ** 3)



# Question - 44 
# Write a program to check whether the given string is palindrome or not.
given_string = input("Enter a string :")
reversed = given_string[::-1]
if given_string == reversed:
    print("Palindrome")
else:
    print("Not a Palindrome")
    
    
# Question - 45 
# Write a program to consider string input, if it is having more than three characters then print length of the string else print string as it is.

input_string = input("Enter a string :")
if len(input_string) > 3:
    print(len(input_string))
else:
    print(input_string)



# Question - 46 
# Write a program to check whether the user is eligible to vote or not.
age = int(input("Enter an age :"))
if age > 18:
    print("Eligible to Vote. ")
else:
    print("Not Eligible to Vote")


# Question - 47 
# Write a program to check whether a number is divisible by 7 or not.
number = int(input("Enter a number :"))
if number % 7 == 0:
    print("Number is Divisible by 7")
else:
    print("Not Divisible by 7")
    
    
# Question - 48 
# Write a program to check whether the last digit of a number entered by the user is divisible by three or not.

number = int(input("Enter a number :"))
last_digit = number % 10 
if last_digit % 3 == 0:
    print("Divisible by 3")
else:
    print("Not Divisible by 3")


# Question - 49  (Good Question ****)
# Write a program to check whether the year is leap year or not.

# main concept is , if any year is completely divided by 4, it become leap year. otherwise not a leap year.
# there is one condition for century year - 2100, for century year we need to separately check it.
# if year is divided by 100 (checking for  century year), then check is it completely divisible by 400, if yes, then leap year...rest not a leap year. 

year = int(input("Enter a year :"))  # 2024 
if year % 4 == 0:
    if year % 100 == 0:    # checking for century year
        if year % 400 == 0:  # if it is century year, does that divisible by 400
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:  # it means divisble by 4
        print("Leap Year")
    
else:
    print("Not a leap year")










# Question - 50
# Write a program to check whether a number entered is a 3 digit number or not.
number_entered = input("Enter a number :")
if len(number_entered) == 3:    # len function always work for collection, not work for int
    print("Entered Number is a 3 digit number.")
else:
    print("Entered number is not a 3 digit number.")
    
    
# Question - 51 
# Write a program to find the largest number out of two numbers expected from the user.
num1 = int(input("Entter a number 1:"))
num2 = int(input("Enter a number 2"))
if num1 > num2:
    print(f"{num1} is Greatest.")
else:
    print(f"{num2} is Greatest. ")



# Question - 52 
# Write a program to check whether a number Entered by the user is positive or negative.
number = int(input("Enter a number :"))
if number > 0:
    print("Positive Number ")
else:
    print("Negative Number")
    
    
# Question - 53
# Write a program.To check whether a number accepted from the user is divisible by two and three both.

number = int(input("Enter a number :"))
if (number % 2 == 0) and (number % 3 == 0):
    print("The number is divisible by both 2 & 3")
else:
    print("The number is not divisible by both 2 & 3")





