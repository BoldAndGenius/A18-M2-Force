# Question - 61 
# Write a program to check if the middle value of heterogeneous tuple collection is integer or not.

het_tup = (1, True, 3+5j, 34, [1,2])   
middle_index = len(het_tup) // 2    # Floor Division - to get the exact integer value, no float value
middle_value = het_tup[middle_index]

if isinstance(middle_value,int):
    print("Middle Value of Heterogeneour Tuple Collection is Integer")
else:
    print("Not an Integer")


# Concept Learned -

'''

The isinstance() function in Python is used to check if an object is of a specific data type or class. It returns True if the object is an instance of the specified class or type, and False otherwise.

Syntax:


isinstance(object, classinfo)

object: The variable or value you want to check.
classinfo: The class, type, or a tuple of classes/types to check against.


'''



# Question - 62 -
# Write a program to check if the given data is individual data type or not.

# individual data type means, (int, float, str, bool, complex) and not a collection data type (like list, tuple, set, dict)


# the easiest way to solve this question is, use isinstance() function

data = eval(input("Enter any data :"))
if isinstance(data, (int, float,complex,bool)):
    print("Individual Data Type")
else:
    print("Not an individual data type")
    
    
    


# Question - 63 

# write a program to check whether the given integer single digit or two digits or three digits or more than three digits


given_integer = input("Enter an integer :")
length_of_integer = len(given_integer)  # len() function only applies to string
if length_of_integer == 1:
    print("Single Digit.")
elif length_of_integer == 2:
    print("Two Digit.")
elif length_of_integer == 3:
    print("Three Digit.")
else:
    print("More than three Digits.")
    
    
    
# Question - 64 
# write a program to print ‘Fizz’ if the given number is multiple of three print, ‘buzz’ if the given number is multiple of 5, and print ‘Fizzbuzz’ if the number is multiple of both 3 and 5.



given_number = int(input("Enter a number :"))
if (given_number % 3 == 0) and (given_number % 5 == 0):
    print("Fizzbuzz")
elif given_number % 5 == 0:
    print("buzz")
elif given_number % 3 == 0:
    print("Fizz")
else:
    print("Invalid Number")




# Question - 65 
# Write a program to predict grade of the student based on the obtained result.
'''
90 to 100 - A+
80 to 90 - A 
70 to 80 - B
60 to 70 - C
35 to 60 - D
<35 - F


Use if elif ladder - since multiple conditions are there, and corresponding statement should be there.
'''

marks = float(input("Enter a marks :"))
if  90 < marks <= 100:
    print("A+ Grade") 
elif 80 < marks <= 90:
    print("A Grade")
elif 70 < marks <= 80:
    print("B Grade")
elif 60 < marks <= 70:
    print("C Grade")
elif 35 < marks <= 60:
    print("D Grade")
elif marks <= 35:
    print("F Grade")
else:
    print("Invalid Grade")
    
    
    
# Question - 66 
# Write a program to check whether the entered character is uppercase or lowercase or number or special character

entered_character = input("Enter a character :")
if entered_character.isupper():
    print("Uppercase")
elif entered_character.islower():
    print("Lowercase")
elif entered_character.isdigit():
    print("Digit")
else:
    print("Special Character")



# Question - 67
# Write a program to find the greatest among two numbers

num1 = float(input("Enter a number 1 :"))
num2 = float(input("Enter a number 2 :"))
if num1 > num2:
    print(f"{num1} is greatest.")
else:
    print(f"{num2} is greatest.")



# Question - 68 
# Write a program to find the smallest among three numbers 

num1 = int(input("Enter a number 1 :"))
num2 = int(input("Enter a number 2 :"))
num3 = int(input("Enter a number 3 :"))

if (num1 < num2) and (num1 < num3):
    print(f"{num1} is Smallest.")
elif (num2 < num1) and (num2 < num3):
    print(f"{num2} is Smallest.")
elif (num1 == num2 == num3):
    print("All three numbers are equal.")
else:
    print(f"{num3} is Smallest.")



# Question - 69
# Write a program to find the greatest among four numbers

num1 = int(input("Enter a number 1 :"))
num2 = int(input("Enter a number 2 :"))
num3 = int(input("Enter a number 3 :"))
num4 = int(input("Enter a number 4 :"))


if (num1 > num2) and (num1 > num3) and (num1 > num4):
    print(f"{num1} is Greatest.")
elif (num2 > num1) and (num2 > num3) and (num2 > num4):
    print(f"{num2} is Greatest.")
elif (num3 > num1) and (num3 > num2) and (num3 > num4):
    print(f"{num3} is Greatest.")
else:
    print(f"{num4} is Greatest.")





# Question - 70
# Write a program to find the smallest among four numbers


num1 = int(input("Enter a number 1 :"))
num2 = int(input("Enter a number 2 :"))
num3 = int(input("Enter a number 3 :"))
num4 = int(input("Enter a number 4 :"))


if (num1 < num2) and (num1 < num3) and (num1 < num4):
    print(f"{num1} is Smallest.")
elif (num2 < num1) and (num2 < num3) and (num2 < num4):
    print(f"{num2} is Smallest.")
elif (num3 < num1) and (num3 < num2) and (num3 < num4):
    print(f"{num3} is Smallest.")
else:
    print(f"{num4} is Smallest.")






