'''All programs written by Rahemat J; 
    githubID:rahematjkd2'''

"""*************** Input and output statements ***************"""

'''1.Write a program to print the square of a given integer number'''

# num = int(input("Enter an integer number: "))
# square = num * num
# print(f"Sqaure of {num} is -> {square}")


'''2. Write a program to find the product of two float numbers.'''

# num1 = float(input("Enter 1st float number: "))
# num2 = float(input("Enter 2nd float number: "))
# print(f"The product of {num1} and {num2} is -> {num1 * num2}")

'''3. Write a program to find the area of a rectangle.'''

# length = eval(input("Enter length of the rectangle: "))
# breadth = eval(input("Enter breadth of the rectangle: "))
# area = length * breadth
# print(f"The Area of given rectangle is -> {area}")

'''4. Write a program to reverse the given string.'''

# str = input("Enter a String: ")
# reverse_str = str[::-1]
# print(f"The reverse of {str} is -> {reverse_str}")

'''5. Write a Program to find the sum, difference, product and division.Between 2 integer numbers.'''

# num1 = int(input("Enter 1st integer: "))
# num2 = int(input("Enter 2nd integer: "))
# print(f'''Sum of {num1} and {num2} is -> {num1 + num2}
# Difference of {num1} and {num2} is -> {num1 - num2}
# Product of {num1} and {num2} is -> {num1 * num2}
# Division of {num1} and {num2} is -> {num1 / num2}''')

'''6. Write a program to find the simple interest.'''

# principal = int(input("Enter principal amount: "))
# time = int(input("Enter time: "))
# roi = eval(input("Enter rate of interest: "))

# simple_interest = (principal * time * roi) / 100

# print(f'''
# Principal Amount : Rs.{principal}
# Time Period : {time} years
# Rate of Interest : {roi}%

# The Simple Interest is -> Rs.{simple_interest}
# ''')

'''7. Write a program to calculate area of triangle'''

# base = eval(input("Enter base of a triangle: "))
# height = eval(input("Enter height of a triangle: "))

# area_of_triangle = 0.5 * base * height

# print(f"The area of given Triangle is -> {area_of_triangle}")

'''8. Write a Python code to swap two variables.'''

# var1 = input("Enter first value: ")
# var2 = input("Enter second value: ")
# print(f"Before Swap\n {var1} {var2}")
# temp = var1
# var1 = var2
# var2 = temp
# print(f"After Swap\n {var1} {var2}")

'''9. Write a Python program to calculate the square root of a given number'''

# # import math
# num = int(input("Enter an integer number: "))
# # square_root = math.sqrt(num)
# square_root = num ** (1/2)
# print(f"The square root of {num} is -> {square_root}")


'''10. Write a Python program to find the area of a circle.'''

# PI = 3.14159265359

# radius = float(input("Enter the radius of a circle: "))
# area_of_circle = PI * (radius ** 2)
# print(f"The Area of a given circle is -> {area_of_circle}")

"""*************** Simple If ***************"""

'''11. Write a program To register.For a company only if job location is Bangalore.'''

# location = input("Enter the location: ")
# if location == 'Bangalore':
#     print("You are eligible to register for this Job")


'''12. Write a program to check whether the given number is even '''

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"The number {num} is an Even Number...")

'''13. Write a program to check whether the given number is odd '''

# num = int(input("Enter a number: "))
# if num % 2 != 0:
#     print(f"The number {num} is an ODD Number...")

'''14. Write a program to check whether the given number lies between 5 to 10'''

# number = int(input("Enter a number: "))
# if number in range(5,11):
#     print(f"The number {number} lies between 5 to 10...")

'''15. Write a program To check whether the given string is having more than three characters '''

# str = input("Enter a String: ")
# if len(str) > 3:
#     print(f"The String {str} contains more than 3 characters i.e. -> {len(str)} characters")

'''16. Write a program To check whether the given number is having 4 digits '''

# num = int(input("Enter a number: "))
# if len(str(num)) == 4:
#     print(f"The number {num} contains exactly {len(str(num))} digits...")

'''17. Write a program to check whether the given character is a vowel '''

# character = input("Enter a character: ")
# if character in ("aeiouAEIOU"):
#     print(f"The character {character} is a vowel...")

'''18. Write a program to check whether the given integer number is even and multiple of five'''

# number = int(input("Enter an integer number: "))
# if number % 2 == 0 and number % 5 == 0:
#     print(f"The number {number} is an Even number and Multiple of 5...")

'''19. Write a program.To check whether the given string is character '''

# str = input("Enter a string: ")
# if len(str) == 1:
#     print(f"The string {str} is a character...")

'''20. Write a program.To check whether the given character is uppercase alphabet '''

# char = input("Enter a single character: ")
# if char.isupper():
#     print(f"The character {char} is an UpperCase Alphabet...")

'''21. Write a program.To check whether the given character is lowercase alphabet '''

# char = input("Enter a single character: ")
# if char.islower():
#     print(f"The character {char} is an LowerCase Alphabet...")

'''22. Write a program to check whether the given character is digit '''

# character = input("Enter a character: ")
# if character.isdigit():
#     print(f"The character {character} is a Digit...")

'''23. Write a program to check whether the given character is alphabet '''

# character = input("Enter a character: ")
# if character.isalpha():
#     print(f"The character {character} is a Alphabet...")

'''24. Write a program to check whether the given character is a special character '''

# char = input("Enter a character: ")
# if not(char.isalnum()):
#     print(f"The character {char} is a Special Character...")

'''25. Write a program to check whether the given collection is List '''

# collection = eval(input("Enter a collection: "))
# if type(collection) is list :
#     print(f"The collection {collection} is a List Data Type...")

'''26. Write a program to check whether the entered value is default '''

# val = eval(input("Enter a value: "))
# if bool(val) == False:
#     print(f"The value entered {val} is a Default Value...")

'''27. Write a program to check whether The list consists of even number of values '''

# user_list = list(input("Enter an integer list: "))
# if (len(user_list) % 2) == 0:
#     print(f"The list {user_list} contains even number of elements...")
#     print(len(user_list))
# else:
#     print(len(user_list))

'''28. Write a program to check whether a list consists of middle value '''

# user_list = [True, 11, "Hello", 2.33, ("this", "is", "tuple")]
# if len(user_list) % 2 != 0:
#     mid_idx = len(user_list) // 2
#     print(f"List contains Middle value at {mid_idx} -> {user_list[mid_idx]}")

'''29. Write a program to check whether the entered input is.Immutable. '''

# user_input = eval(input("Enter input: "))
# if type(user_input) in (str, tuple):
#     print(f"The input {user_input} is an Immutable DataType...")
    
'''30. Write a program to check whether the entered input is mutable.'''

# user_input = eval(input("Enter input: "))
# if type(user_input) not in (str, tuple):
#     print(f"The input {user_input} is a Mutable DataType...")  
    
'''31. Write a program to check whether The entered input is a single value '''

# user_input = eval(input("Enter input: "))
# if type(user_input) in (int, float, complex, bool):
#     print(f"The input < {user_input} > is a Single Value DataType...")

'''32. Write a program to check whether the entered input is multivalue or not.'''

# user_input = eval(input("Enter input: "))
# if type(user_input) not in (int, float, complex, bool):
#     print(f"The input < {user_input} > is a Multi Value DataType...")

'''33. Write a program to check whether the entered number is having only single Digit.'''

# num = int(input("Enter a number: "))
# if len(str(num)) == 1:
#     print(f"The number {num} entered is a Single Digit Number...")

"""*************** If else ***************"""

'''34. Uni whether the first value present inside the given list is complex or not.'''

# user_list = eval(input("Enter a collection: "))
# if type(user_list[0]) is complex:
#     print(f"The first element {user_list[0]} is a Complex...")

'''35. Write a program to take and consider a tuple collection consisting of only two values. Check whether the taken tuple is homogeneous or heterogeneous.'''

# user_tple = eval(input("Enter a Tuple with only 2 values: "))
# if type(user_tple[0]) == type(user_tple[1]):
#     print(f"The tuple < {user_tple} > is a Homogenous Tuple...")

'''36. Write a program to check whether the given integer number is multiple of 10 or not.'''

# num = int(input("Enter an integer: "))
# if num % 10 == 0:
#     print(f"The entered number < {num} > is a Multiple of 10...")

'''37. Write a program to consider an integer number. If the number is even then print square of the number else print the cube of the number.'''

# num = int(input("Enter an Integer: "))
# if num % 2 == 0:
#     print(f"The Number {num} is an Even number. So Square of {num} is -> {num ** 2}...")
# else:
#     print(f"The Number {num} is NOT an Even number. So Cube of {num} is -> {num ** 3}...")

'''38. Write a program to check whether the given string is palindrome or not.'''

# input_str = input("Enter a string: ")
# reversed_str = input_str[::-1]
# if input_str == reversed_str:
#     print(f"The String {input_str} is a Palindrome -> {reversed_str}")

'''39. Write a program to consider string input, if it is having more than three characters then print length of the string else print string as it is.'''

# input_str = input("Enter a string: ")
# if len(input_str) > 3:
#     print(f"The string is a {len(input_str)} character String...")
# else:
#     print(f"The string does not contain more than 3 characters. So -> {input_str}")

'''40. Write a program to check whether the user is eligible to vote or not.'''

# age = int(input("Enter your Age: "))
# if age >= 18:
#     print("You are Eligible to vote...")

'''41. Write a program to check whether a number is divisible by 7 or not.'''

# num = int(input("Enter an integer: "))
# if num % 7 == 0:
#     print(f"The entered number < {num} > is Divisible by 7...")

'''42. Write a program to check whether the last digit of a number entered by the user is divisible by three or not.'''

# num = input("Enter a number: ")
# if int(num[-1]) % 3 == 0:
#     print(f"The last digit {num[-1]} of number {num} is Divisible By 3...")

'''43. Write a program to check whether the year is leap year or not.'''

# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     print(f"{year} is a Leap Year...")

'''44. Write a program to check whether a number entered is a 3 digit number or not.'''

# num = input("Enter a number: ")
# if len(num) == 3:
#     print(f"{num} has 3 digits...")

'''45. Write a program to find the largest number out of two numbers expected from the user.'''

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# if num1 > num2:
#     print(f"Number 1 - {num1} is Largest...")
# else:
#     print(f"Number 2 - {num2} is Largest...")

'''46. Write a program to check whether a number.Entered by the user is positive or negative.'''

# num = int(input("Enter a Number: "))
# if num > 0:
#     print(f"{num} is a Positive Number")
# else:
#     print(f"{num} is a Negative Number")

'''47. Write a program.To check whether a number accepted from the user is divisible by two and three both.'''

# num = int(input("Enter a Number: "))
# if num % 2 == 0 and num % 3 == 0:
#     print(f"The number < {num} > is divisible by 2 and 3...")

"""*************** Elif Statement ***************"""

'''48.Write a program to check the relation between two integer numbers'''

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 < num1:
#     print(f"{num2} is less than {num1}")
# elif num1 == num2:
#     print(f"{num1} is Exactly equals to {num2}")

'''49. Write a program to check whether a given character is uppercase or lowercase or number. If character is uppercase print uppercase, If character is lowercase print lowercase. If the character is a number, print the ascii number of it. '''

# char = input("Enter a Character: ")
# if char.isupper():
#     print("Character is an Uppercase character...")
# if char.islower():
#     print("Character is an Lowercase character...")
# if char.isdigit():
#     print(f"The ASCII value of {char} is -> {ord(char)}")

'''50. Write a program to check whether a given character is a vowel or consonant. If a given character is a vowel, store the character inside the list. If a given character is consonant, display the ASCII value of that character. '''

# vowel = []
# char = input("Enter a character: ")
# if char in "aeiouAEIOU":
#     vowel.append(char)
#     print(f"The character {char} is an Vowel therefore it is stored inside the List-> {vowel}")
# else:
#     print(f"The character {char} is Consonant. It's ASCII value is -> {ord(char)}")

'''51. Write a program to check if the given data is individual data type or not. '''

# user_input = eval(input("Enter input: "))
# if type(user_input) in (int, float, complex, bool):
#     print(f"The input < {user_input} > is a Individual DataType...")
# else:
#     print(f"The input < {user_input} > is not an Individual DataType...")

'''52. write a program to check whether the given integer single digit or two digits or three digits or more than three digits'''

# integer = int(input("Enter an Integer: "))
# if integer in range(0, 10):
#     print(f"{integer} is a Single Digit Integer...")
# elif integer in range(10, 100):
#     print(f"{integer} is a Two Digit Integer...")
# elif integer in range(100, 1000):
#     print(f"{integer} is a Three Digit Integer...")
# else:
#     print(f"{integer} is More Three Digit Integer...")
    
"""53. write a program to print 'Fizz' if the given number is multiple of 3, 
print 'buzz' if the given number is multiple of 5 and 
print 'Fizzbuzz' if the number is multiple of both 3 and 5"""

# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("Fizzbuzz...")
# elif num % 3 == 0:
#     print('Fizz...')
# elif num % 5 == 0:
#     print('buzz...')

'''54. Write a program to predict grade of the student based on the obtained result '''

# marks = int(input("Enter the Marks: "))
# if marks in range(90, 100):
#     print("Grade S")
# elif marks in range(80, 90):
#     print("Grade A")
# elif marks in range(70, 80):
#     print("Grade B")
# elif marks in range(60, 70):
#     print("Grade C")
# elif marks in range(50, 60):
#     print("Grade D")
# elif marks in range(40, 50):
#     print("Grade E")
# else:
#     print("Failed...")

'''55. Write a program to check whether the entered character is uppercase or lowercase or number or special character'''

# char = input("Enter a character: ")
# if char.isupper():
#     print(f"{char} is an Upper Case Character...")
# elif char.islower():
#     print(f"{char} is an Lower Case Character...")
# elif char.isnumeric():
#     print(f"{char} is an Numeric Character...")
# else:
#     print(f"{char} is an Special Character...")

'''56. Write a program to find the greatest among two numbers'''

# num1 = int(input("Enter Number 1: "))
# num2 = int(input("Enter Number 2: "))
# if num1 > num2:
#     print(f"{num1} is greatest...")
# else:
#     print(f"{num2} is greatest...")

'''57. Write a program to find the smallest among three numbers '''

# num1 = int(input("Enter Number 1: "))
# num2 = int(input("Enter Number 2: "))
# num3 = int(input("Enter Number 3: "))
# if num1 < num2:
#     if num1 < num3:
#         print(f"{num1} is Smallest...")
#     else:
#         print(f"{num3} is Smallest...")
# else:
#     if num2 < num3:
#         print(f"{num2} is Smallest...")
#     else:
#         print(f"{num3} is Smallest...")
        
'''58. Write a program to find the greatest among four numbers'''

# num1 = int(input("Enter Number 1: "))
# num2 = int(input("Enter Number 2: "))
# num3 = int(input("Enter Number 3: "))
# num4 = int(input("Enter Number 4: "))
# if num1 > num2 and num1 > num3:
#     if num1 > num4: 
#         print(f"{num1} is greatest...")
#     else:
#         print(f"{num4} is greatest...")
# else:
#     if num2 > num3:
#         if num2 > num4:
#             print(f"{num2} is greatest...")
#         else:
#             print(f"{num4} is greatest...")
#     else:
#         if num3 > num4:
#             print(f"{num3} is greatest...")
#         else:
#             print(f"{num4} is greatest...")

'''59. Write a program to find the smallest among four numbers'''

# num1 = int(input("Enter Number 1: "))
# num2 = int(input("Enter Number 2: "))
# num3 = int(input("Enter Number 3: "))
# num4 = int(input("Enter Number 4: "))
# if num1 < num2 and num1 < num3:
#     if num1 < num4: 
#         print(f"{num1} is Smallest...")
#     else:
#         print(f"{num4} is Smallest...")
# else:
#     if num2 < num3:
#         if num2 < num4:
#             print(f"{num2} is Smallest...")
#         else:
#             print(f"{num4} is Smallest...")
#     else:
#         if num3 < num4:
#             print(f"{num3} is Smallest...")
#         else:
#             print(f"{num4} is Smallest...")

'''60. Write a program to calculate the electricity bill.According to the following criteria, for 1st 100 units there is no charge, For next 100 units there is ₹5 per unit and after 200 units, the price is rupees 10 per unit.If the input is 350 then total bill amount is Rupees 2000. '''

# units = int(input("Enter units consumed: "))
# if units in range(1, 101):
#     print("No charge...")
# elif units in range(101, 201):
#     print(f"Charged at Rs.5 per units -> Rs{(units - 100) * 5}")
# else:
#     charge = 100 * 5
#     charge += (units - 200) * 10
#     print(f"Charged at Rs.10 per units -> Rs{charge}")
    
'''61. Write a program to accept percentages from the user and display the grade according to the following criteria. If marks is greater than 90, grade is A. If marks is greater than 80 and less than equals to 90, gra inde is B if marks is greater than or equal to 60, and less than equals to 80 grade is C, else if it is less than 60 grade is D'''

# percenatge = int(input("Enter the Marks: "))
# if percenatge > 90:
#     print("Grade A")
# elif percenatge in range(80, 91):
#     print("Grade B")
# elif percenatge in range(60, 81):
#     print("Grade C")
# elif percenatge < 60:
#     print("Grade D")
# else:
#     print("Failed...")

'''62. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria 
if cost price is greater than 1Lac.The tax is 50%, 
if it is greater than 50,000 and less than equals to 1,00,000 the tax is 10% and 
if it is less than equals to 50,000 the tax is 5%.'''

# cost = int(input("Enter Cost Price of Your Bike: "))
# if cost > 100000:
#     print(f"Your Cost is Rs.{cost}, The Road Tax will be of 50%\n The Tax amount should be paid of Rs.{cost * (50/100)}...")
# elif cost in range(50001, 100001):
#     print(f"Your Cost is Rs.{cost}, The Road Tax will be of 10%\n The Tax amount should be paid of Rs.{cost * (10/100)}...")
# else:
#     print(f"Your Cost is Rs.{cost}, The Road Tax will be of 5%\n The Tax amount should be paid of Rs.{cost * (5/100)}...")
    
'''63. Write a program to accept a number from one to seven and display the name of the day. Like one for Sunday, 2 for Monday and so on.'''

# num = int(input("Enter a Number: "))
# match num:
#     case 1: print("Sunday")
#     case 2: print("Monday")
#     case 3: print("Tuesday")
#     case 4: print("Wednesday")
#     case 5: print("Thursday")
#     case 6: print("Friday")
#     case 7: print("Saturday")

'''64. Write a program to accept a number from 1:00 to 12:00 and display name of the month and days in that month like one for January and number of days is 31 and so on.'''

# num = int(input("Enter a Number: "))
# match num:
#     case 1: print("January")
#     case 2: print("February")
#     case 3: print("March")
#     case 4: print("April")
#     case 5: print("May")
#     case 6: print("June")
#     case 7: print("July")
#     case 8: print("August")
#     case 9: print("September")
#     case 10: print("October")
#     case 11: print("November")
#     case 12: print("December")

'''65. Accept any city from the user and display monuments of that city. For Delhi it is Red Fort, Agra- Taj Mahal, Jaipur- Jal Mahal.'''

# city = input("Enter any City Name: ")
# print("Monuments -> ", end="")
# match city:
#     case 'delhi': print("Red Fort")
#     case 'agra': print("Taj Mahal")
#     case 'jaipur': print("Jal Mahal")

'''66. Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.'''

# side1 = float(input("Enter the length of the first side: "))
# side2 = float(input("Enter the length of the second side: "))
# side3 = float(input("Enter the length of the third side: "))
# if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
#     if side1 == side2 == side3:
#         print("The given triangle is: Equilateral Triangle")
#     elif side1 == side2 or side2 == side3 or side1 == side3:
#         print("The given triangle is: Isosceles Triangle")
#     else:
#             print("The given triangle is: Scalene Triangle")
# else:
#     print("Not a valid triangle")

'''67. Accept the number of days from the user and calculate the charge of library according to the following criteria. Till five days it is ₹2 per day, 6 to 10 days it is ₹3 per day, 11 to 15 days it is ₹4.00 per day and after 15 days it is 5 Rupees per day.'''

# days = int(input("Enter number of Days: "))
# if days in range(1, 6):
#     print(f"Rs.2 per day Charged. Your Total Charge will be -> Rs.{days * 2}")
# elif days in range(6, 11):
#     print(f"Rs.3 per day Charged. Your Total Charge will be -> Rs.{days * 3}")
# elif days in range(11, 16):
#     print(f"Rs.4 per day Charged. Your Total Charge will be -> Rs.{days * 4}")
# else:
#     print(f"Rs.5 per day Charged. Your Total Charge will be -> Rs.{days * 5}")
    
'''68. Accept the kilometers covered and calculate the bill according to the following criteria. For 1st 10 kilometers it is ₹11.00 per kilometer, For next 90 kilometers it is rupees 10 per kilometer and after that it is ₹9 per kilometer. '''    

# km_covered = int(input("Enter distance covered in Kilometers: "))
# if km_covered <= 10:
#     charge = km_covered * 11
#     print(f"₹11.00 per kilometer will be charged. Your Total Charge will be -> ₹{charge}")
# elif km_covered <= 100:
#     charge = (10 * 11) + ((km_covered - 10) * 10)
#     print(f"₹10.00 per kilometer will be charged. Your Total Charge will be -> ₹{charge}")
# else:
#     charge = (10 * 11) + (90 * 10) + ((km_covered - 100) * 9)
#     print(f"₹9.00 per kilometer will be charged. Your Total Charge will be -> ₹{charge}")
    
'''69. WAP to convert temperature from celsius to kelvin and kelvin to celsius using the elif statement.'''  

# temp = input("Enter temperature in C or K: ")
# if temp[-1] in 'cC':
#     int_part = int(temp[:-1:1])
#     print(f"{int_part} degrees -> {int_part + 273} Kelvin.")
# elif temp[-1] in 'kK':
#     int_part = int(temp[:-1:1])
#     print(f"{int_part} Kelvin -> {int_part - 273} Degrees.")

'''70. Write a program to create an Instagram login page.'''

# instaId = 'abc'
# password = 123
# userId = input("Enter User Name: ")
# userPass = int(input("Enter the Password: "))
# if userId == instaId:
#     if userPass == password:
#         print(f"{userId} Logged In Successfully...")
#     else:
#         print("Invalid Password...")
# else:
#     print("Invalid Username...")

'''71. Program to print middle value of the given heterogeneous tuple collection only if the middle value is string and having the length greater than 3. '''

# hetero_tuple = (1, "Hi", "Rage", True, 3.33)
# mid_idx = len(hetero_tuple) // 2
# if type(hetero_tuple[mid_idx]) is str:
#     if len(hetero_tuple[mid_idx]) > 3:
#         print(f"The Middle Value is a String of Length -> {len(hetero_tuple[mid_idx])} and \nThe value is -> {hetero_tuple[mid_idx]}")

'''72. Write a program to find the second greatest among four numbers.'''

# num1 = int(input("Enter Number 1: "))
# num2 = int(input("Enter Number 2: "))
# num3 = int(input("Enter Number 3: "))
# num4 = int(input("Enter Number 4: "))
# numbers = [num1, num2, num3, num4] #Using List
# sorted_numbers = sorted(numbers, reverse=True)
# print(f"{sorted_numbers[1]} is Second Largest Number...")

'''73. Write a program.To check the type of a given character.'''

# char = eval(input("Enter any Character: "))
# print(type(char))

'''74. Write a program to consider an integer number. Print happy if the number is divisible by 2. Print SAD if the number is divisible by 5 and print square of the numbers only if it is divisible by 7 else print the number as it is.'''

# integer = int(input("Enter an Integer: "))
# if integer % 2 == 0:
#     print("Happy")
# elif integer % 5 == 0:
#     print("SAD")
# elif integer % 7 == 0:
#     print(integer ** 2)
# else:
#     print(integer)

'''75. Program to consider an input string. Print the string as it is if it is palindrome. Print the reverse string if it has an even number of characters. Print all the characters present at an odd index if the string is having an odd number of characters.'''

# string = input("Enter a String: ")
# if string == string[::-1]:
#     print(f"{string}")
# elif len(string) % 2 == 0:
#     print(string[::-1])
# else:
#     print(string[::2])

'''76. Write a program to print middle Character.Given string only if it is upper case character.'''

# string = input("Enter a string: ")
# mid_char = len(string) // 2
# if string[mid_char].isupper():
#     print(string[mid_char])

'''77. Write a program to print the length of given data only if it is even.'''

# data = input("Enter any data: ")
# if len(data) % 2 == 0:
#     print(f"Length of {data} is -> {len(data)}")
# else:
#     print(f"The length of entered data {data} is not Even...")

'''80. Write a program that determines the movie ticket price based on the age and day of the week
Adults (18+): $12 (except for Tuesdays: $10)
Children (under 18): $8 (except for Tuesdays: $6)
Seniors (65+): $8 (always)'''

# day = input("Enter the day: ")
# age = int(input("Enter your age: "))
# if age >= 18 and age < 65:
#     if day != 'tuesday':
#         print(f"You're {age} year old so your ticket price is -> $12...")
#     else:
#         print(f"It's {day} so your ticket price is -> $10...")
# elif age < 18:
#     if day != 'tuesday':
#         print(f"You're {age} year old so your ticket price is -> $8...")
#     else:
#         print(f"It's {day} so your ticket price is -> $6...")
# else:
#     print(f"You're {age} year old so your ticket price is -> $8...")  

'''81. Leap Year Checker: Write a program that determines if a given year is a leap year. A leap year is a year divisible by 4, but not by 100 unless it's also divisible by 400.'''

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a Leap Year...")
# else:
#     print(f"{year} is not a Leap Year...")

'''82. Vending Machine: Create a program for a vending machine that takes product code (integer) and amount paid (float) as input. It should check the product price (stored in a dictionary) and dispense the product if enough is paid. Use nested ifs for different error messages (e.g., invalid code, insufficient funds).'''

# products = {
#     101: 25.00,
#     102: 35.00,
#     103: 50.00,
#     104: 15.00
# }

# prod_code = int(input("Enter the product code: "))
# amount_paid = float(input("Enter the Amount: "))

# if prod_code in products:
#     price = products[prod_code]
#     if amount_paid >= price:
#         change = amount_paid - price
#         print(f"Product {prod_code} is Dispensed. Your change is ₹{change}.")
#     else:
#         print(f"Insufficient funds. The product costs ₹{price}, but you paid ₹{amount_paid}.")
# else:
#     print("Invalid Product code. Please Enter Valid Product Code.")

'''83. Restaurant Discount: Write a program that calculates a restaurant bill with a discount based on the day of the week and party size:
Weekdays (Mon-Fri), party < 4: No discount.
Weekdays (Mon-Fri), party >= 4: 10% discount.
Weekends (Sat-Sun), any party size: 15% discount.'''

# day = input("Enter the day: ")
# party_size = int(input("Enter party size: "))
# weekdays = ("monday", "tuesday", "wednesday", "thursday", "friday")
# if day in weekdays:
#     if party_size < 4:
#         print("Sorry your Discount is -> 0")
#     elif party_size >= 4:
#         print(f"You got 10% discount on your Bill...")
# else:
#     print(f"It's Weekend so you got 15% discount on your Bill...")

'''84. Shape Identifier: Design a program that takes two inputs (length1, length2) and identifies the geometric shape based on the values:
If lengths are equal: Square
If one length is twice the other: Rectangle
Otherwise: Not a square or rectangle'''

# len1 = int(input("Enter the length 1: "))
# len2 = int(input("Enter the length 2: "))

# if len1 == len2:
#     print("Square")
# elif (len1 > (2 * len2)) or (len2 > (2 * len1)):
#     print("rectangle".title())
# else:
#     print("Not a rectangle or square")

'''86. Wap to accept any number from 1 to 5 and display that number in word form. if they enter more than 5 then print no match.'''

# num = int(input("Enter a number: "))
# match num:
#     case 1: print("One")
#     case 2: print("Two")
#     case 3: print("Three")
#     case 4: print("Four")
#     case 5: print("Five")
#     case _: print("No match")

'''87. WAP to take input as only collections. 
i) if the type of input is a list then  ask the value from the user and insert it in the middle index of that list. and print that list.
ii) if type of input is tuple print 'cannot append tuple is immutable'
iii)if type is set, take the input from the user. if the value is immutable then only add it to the set and print the set otherwise print 'enter only immutable collection'
iv) if type of input is dictionary take key and value as user input and add the key and value 	pair using syntax to add key value . and print the dictionary.'''

# user_input = eval(input("Enter collections: "))
# user_list = []
# user_set = set()
# user_dict = {}
# if type(user_input) is list:
#     value = eval(input("Enter the value to add inside the list: "))
#     mid_idx = len(user_list) // 2
#     user_list.insert(mid_idx, value)
#     print(user_list)
# elif type(user_input) is tuple:
#     print("Cannot append, tuple is immutable...")
# elif type(user_input) is set:
#     items = eval(input("Enter items to add in set: "))
#     if type(items) in (str, tuple):
#         user_set.add(items)
#         print(user_set)
# elif type(user_input) is dict:
#     key = eval(input("Enter a key: "))
#     value = eval(input("Enter a value: "))
#     if type(key) not in (list, set):
#         user_dict[key] = value
#         print(user_dict)