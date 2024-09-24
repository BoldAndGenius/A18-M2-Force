######################################################################
######################################################################
'''SIMPLE IF'''

# 11.Write a program To register.For a company only if job location is Bangalore.
job_location = input("Enter the job location:")
if job_location=="bangalore":
    name = input("Enter your name:")
    email = input("Enter your Email-ID:")
    phno = int(input("Enter your phone number:"))
    password = input("Enter your Password:")
    print("Registration Successful")


# 12.Write a program to check whether the given number is even 
num = int(input("Enter a number:"))
if num % 2 == 0:
    print(f"{num} is a even number")
    

# 13. Write a program to check whether the given number is odd 
num = int(input("Enter num:"))
if num % 2 != 0:
    print(f"The given number {num} is Odd")


# 14.Write a program to check whether the given number lies between 5 to 10 
 num = int(input("Enter a number:"))
if 5 < num < 10:
    print(f"{num} lies between 5 to 10")
    
    
# 15.Write a program To check whether the given string is having more than three characters 
word = input("Enter word:")
if len(word) > 3:
    print(f"The {word} has more than three characters")


# 16. Write a program.To check whether the given number is having.4 digits 
num = int(input("Enter num:"))
if -9999 <= num <= 9999:
    print(f"{num} has 4 digits")
    
    
# 17.Write a program to check whether the given character is a vowel 
char = input("Enter a character:")
if char in "aeiouAEIOU":
    print(f"{char} is a vowel")
    
# 18.Write a program to check whether the given integer number is even and multiple of five
num = int(input("Enter num:"))
if (num % 2 == 0) and (num % 5 == 0):
    print(f"{num} is even and multiple of 5") 
    

# 19.Write a program.To check whether the given string is (single) character 
string = input("Enter a string:")
if len(string) == 1:
    print(f"{string} has a single character")
    

# 20.Write a program.To check whether the given character is uppercase alphabet 
char = input("Enter char:")
if char.isupper():
    print(f"{char} is a uppercase alphabet")  


# 21.Write a program To check whether the given character is lowercase alphabet 
char = input("Enter a character:")
if char.islower():
    print(f"{char} is a lowercase alphabet")


# 22.Write a program to check whether the given character is digit 
char = input("Enter char:")
if char.isnumeric():
    print(f"{char} is a digit")
    

# 23.Write a program to check whether the given character is alphabet 
char = input("Enter a character:")
if char.isalpha():
    print(f"{char} is a alphabet")

   
# 24.Write a program to check whether the given character is a special character
char = input("Enter char:")
if not(char.isalnum()):
    print(f"{char} is a Special character")  
    

# 25.Write a program to check whether the given collection is List 
collection = eval(input("Enter a collection:"))
if type(collection) == list:
    print("The given collection is a list")


# 26.Write a program to check whether the entered value is default
value = eval(input("Enter value:"))
if value == '':
    print("String default value ")
if value == []:
    print("List default value")
if value == ():
    print("Tuple default value")
if value == set():
    print("Set default value")
if value == {}:
    print("Dictionary default value")


# 27.Write a program to check whether The list consists of even number of values 
list1 = eval(input("Enter a list:"))
if len(list1) % 2 == 0:
    print("The list consists even number of values")


# 28.Write a program to check whether a list consists of middle value
list1 = eval(input("Enter a list"))
if len(list1) % 2 != 0:
    print("The list consists of middle values")


# 29.Write a program to check whether the entered input is.Immutable.
collection = eval(input("Enter any data:"))
if type(collection) in [str,tuple]:
    print("The collection is Immutable")


# 30.Write a program to check whether the entered input is mutable.
collection = eval(input("Enter collection:"))
if type(collection) in [list,set,dict]:
    print(f"{collection} is mutable")


# 31.Write a program to check whether The entered input is a single value 
value = eval(input("Enter any value:"))
if type(value) in [int,float,complex,bool]:
    print(f"The {value} is a single value")
    

# 32.Write a program to check whether the entered input is multivalue or not.
collection = eval(input("Enter collection:"))
if type(collection) in [str,list,tuple,set,dict]:
    print(f"{collection} is Multivalue datatype")


# 33.Write a program to check whether the entered number is having only single Digit.
digit = int(input("Enter a digit:"))
if -9 <= digit <= 9:
    print(f"{digit} is a single digit")




#######################################################################
#######################################################################
'''IF ELSE'''

# 34.Write a program to check whether the first value present inside the given list is complex or not.
items=eval(input('Enter a list of values :'))
if type(items[0])==complex:
    print(f"Datatype of {items[0]} is complex ")
else:
    print(f"Datatype of {items[0]} is not complex ")


# 35.Write a program to take and consider a tuple collection consisting of only two values. Check whether the taken tuple is homogeneous or heterogeneous.
items=eval(input('Enter two items of a tuple :'))
if type(items[0])==type(items[1]):
    print(f"{items} is a homogeneous tuple")
else:
    print(f"{items} is a heterogeneous tuple")


# 36.Write a program to check whether the given integer number is multiple of 10 or not.
number = int(input('Enter a number :'))
if number%10==0:
    print(f"{number} is multiple of 10")
else:
    print(f"{number} is not multiple of 10")
    

# 37.Write a program to consider an integer number. If the number is even then print square of the number else print the cube of the number
num = int(input("enter the number :"))
if num%2==0:
    print(f"{num} is a even number and its square is:{num**2}")
else :
    print(f"{num} is not a even number and its cube is:{num**3}")


# 38.Write a program to check whether the given string is palindrome or not.
string = input('Enter a string :')
reverse=string[::-1]
if reverse==string:
    print(f"{string} is a palindrome...")
else:
    print(f"{string} is not a palindrome...")


# 39.Write a program to consider string input, if it is having more than three characters then print length of the string else print string as it is.
word = input("Enter word:")
if len(word) > 3:
    print(f"Length of the string is {len(word)}")
else:
    print(f"String is {word}")


# 40.Write a program to check whether the user is eligible to vote or not
age = int(input('Enter age :'))
if age>=18:
    print('Congratulations you are eligible to vote')
else:
    print('Not eligible to vote')


# 41.Write a program to check whether a number is divisible by 7 or not.
num = int(input("Enter num:"))
if num % 7 == 0:
    print(f"{num} is divisible by 7")
else:
    print(f"{num} is not divisible by 7")
    
    
# 42.Write a program to check whether the last digit of a number entered by the user is divisible by three or not.
num = int(input("Enter a number:"))
last_digit = num % 10
if last_digit % 3 == 0:
    print(f"The last digit {last_digit} of number {num} is divisible by 3.")
else:
    print(f"The last digit {last_digit} of number {num} is not divisible by 3.")


# 43.Write a program to check whether the year is leap year or not.
year = int(input("Enter year:"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
    
    
# 44.Write a program to check whether a number entered is a 3 digit number or not.
number = int(input("enter a number :"))
if (number>99 and number<1000) or (number<-99 and number>-1000):
    print(f"{number} is three digit number")
else:
    print(f"{number} is not three digit number")
                      # or
num = int(input("Enter a number:"))
if (num <= -999) or (num >= 999):
    print(f"{num} is a three-digit number")
else:
    print(f"{num} is not a three-digit number")
       
       
# 45.Write a program to find the largest number out of two numbers expected from the user.
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
if num1 > num2:
    print(f"{num1} is largest number than {num2}")
else:
    print(f"{num2} is largest number than {num1}")


# 46.Write a program to check whether a number.Entered by the user is positive or negative.
num = int(input("Enter a number:"))
if num >= 0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a negative number")


# 47.Write a program.To check whether a number accepted from the user is divisible by two and three both.
num = int(input("Enter num:"))
if (num % 2 == 0) and (num % 3 == 0):
    print(f"{num} is divisible by 2 and 3")
else:
    print(f"{num} is not divisible by 2 and 3" )


#######################################################################
#######################################################################
'''ELIF'''

# 54. Write a program to check the relation between two integer numbers
num_1= int(input("enter the num 1: "))
num_2= int(input("enter the num 2: "))
if num_1 == num_2:
    print('Both Numbers are equal')
elif num_1 > num_2:
    print("Number 1 is greater than Number 2")
else:
    print("Number 2 is greater")


# 55. Write a program to check whether a given character is uppercase or lowercase or number. If character is uppercase print uppercase, If character is lowercase print lowercase. If the character is a number, print the ascii number of it.
char = input("Entrer a char: ")
if char.isnumeric():
    print(ord(char))
elif char.isupper():
    print("Char is upper case")
elif char.islower():
    print("char is lower case")
else:
    print("char is nither upper case nor lowercase nor number")


# 56. Write a program to check whether a given character is a vowel or consonant. If a given character is a vowel, store the character inside the list. If a given character is consonant, display the ASCII value of that character.
character = input("enter a alphabet: ")
vovel= []
if character.lower() in ['a','i','o','u','e']:
    vovel.append(character)
elif character.lower() in "bcdfghjklmnpqrstvwxyz":
    print(ord(character))
else:
    print("It is not an alphabet")

# 57. Write a program to check whether a given character is uppercase. If it is uppercase, convert it to lowercase.Else PRINT LOWERCASE.
char= input("enter a alphabet: ")
if char.isupper():
    print(char.lower())
else:
    print("It LOWER CASE")

# 58. Write a program to checkWhether the entered character is a number. If it is a number, print the ASCII value of that number.
character = input("Enter a character: ")
if character.isdigit():
    ascii_value = ord(character)  
    print(f"The ASCII value of '{character}' is: {ascii_value}")
else:
    print(f"The character '{character}' is not a number.")


# 59. Write a program to check whether given character is uppercase, print its lowercase character or if given character is lowercase print its uppercase character or if given character is special character print the character after adding 8 to the ascii value of that particle special character
char = input("enter the char: ")
if char.isupper():
    print(char.lower())
elif char.islower():
    print(char.upper())
elif char.isnumeric():
    print("Invalid Input")
else:
    print(ord((char))+8)
    
    
# 60. Write a program to check whether the last character of a given string is a special character or not.
char = input("enter a string: ")
if char[-1].isalnum():
    print("It is not a special character")
else:
    print("It is a special character")


# 61. Write a program to check if the middle value of heterogeneous tuple collection is integer or not.
tpl= eval(input("enter a tupple: "))
mid_index= len(tpl) // 2
mid_value = tpl[mid_index]

if type(mid_value) == int:
    print("The middle value is Integer")
else:
    print("The middle value is not integer")


# 63. write a program to check whether the given integer single digit or two digits or three digits or more than three digits
num= int(input("enter a number: "))
if -9 <= num <= 9:
    print("It is a single digit")
elif -99 <= num <= 99:
    print("It is a two digit")
elif -999 <= num <= 999:
    print("It is three digit")
else:
    print("It is more than three digit")


# 65. Write a program to predict grade of the student based on the obtained result
marks = int(input('Enter your marks: '))
if marks < 0 or marks > 100:
    print("Invalid input! Marks should be between 0 and 100.")
else:
    if marks >= 90:
        print('Grade A')
    elif marks >= 80:
        print('Grade B')
    elif marks >= 70:
        print('Grade C')
    elif marks >= 60:
        print('Grade D')
    elif marks >= 50:
        print('Grade E')
    else:
        print('Fail')


# 66. Write a program to check whether the entered character is uppercase or lowercase or number or special character
char = input("enter the char: ")
if char.isupper():
    print("The character is uppercase")
elif char.islower():
    print("The character is lowercase")
elif char.isnumeric():
    print("The character is numeric")
else:
    print("The character is a special character")


# 67. Write a program to find the greatest among two numbers
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

if num_1 > num_2:
    print(f"The greatest number is: {num_1}")
elif num_2 > num_1:
    print(f"The greatest number is: {num_2}")
else:
    print("Both numbers are equal.")


# 68. Write a program to find the smallest among three numbers
num_1 = float(input('enter a number'))
num_2 = float(input('enter a number'))
num_3 = float(input('enter a number'))
if num_1 <= num_2 and num_1 <= num_3:
    print(f"{num_1}")
elif num_2 <= num_1 and num_2 <= num_3:
    print(num_2)
else:
    print(num_3)


# 69. Write a program to find the greatest among four numbers
num_1 = float(input('enter a number 1: '))
num_2 = float(input('enter a number 2: '))
num_3 = float(input('enter a number 3: '))
num_4 = float(input('enter a number 4: '))
if num_1 >= num_2 and num_1 >= num_3 and num_1 >= num_4:
    print(f"Number 1 is the greatest: {num_1}")
elif num_2 >= num_1 and num_2 >= num_3 and num_2 >= num_4:
    print(f"Number 2 is the greatest: {num_2}")
elif num_3 >= num_1 and num_3 >= num_2 and num_3 >= num_4:
    print(f"Number 3 is the greatest: {num_3}")
else:
    print(f"Number 4 is the greatest: {num_4}")


# 71. Write a program to calculate the electricity bill.According to the following criteria, for 1st 100 units there is no charge, For next 100 units there is ₹5 per unit and after 200 units, the price is rupees 10 per unit.If the input is 350 then total bill amount is Rupees 2000.
units= int(input("Enter the units: "))
Total_Bill= 0.0
if 0 <= units <= 100:
    Total_Bill = 0.0
elif 0<= units <= 200:
    Total_Bill = (units-100)*5
elif units > 200:
    Total_Bill = (units-200)*10 + (100*5)
print(f"The total bill for {units} units is Rs {Total_Bill}")


# 72. Write a program to accept percentages from the user and display the grade according to the following criteria. If marks is greater than 90, grade is A. If marks is greater than 80 and less than equals to 90, gra inde is B if marks is greater than or equal to 60, and less than equals to 80 grade is C, else if it is less than 60 grade is D
marks = int(input('Enter your marks: '))
if marks < 0 or marks > 100:
    print("Invalid input! Marks should be between 0 and 100.")
else:
    if marks > 90:
        print('Grade A')
    elif marks > 80 and marks <= 90:
        print('Grade B')
    elif marks >= 60 and marks <= 80:
        print('Grade C')
    else:
        print('Grade D')


# 80. WAP to convert temperature from celsius to kelvin and kelvin to celsius using the elif statement.
print("Temperature Conversion Options: \n1. Celsius to Kelvin \n2. Kelvin to Celsius")
choice = input("Enter the number of your choice (1 or 2): ")
if choice == '1':
        # Convert Celsius to Kelvin
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius} Celsius is equal to {kelvin:.2f} Kelvin.")
elif choice == '2':
        # Convert Kelvin to Celsius
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin} Kelvin is equal to {celsius:.2f} Celsius.")  
else:
        print("Invalid choice. Please enter 1 or 2.")


#######################################################################
#######################################################################
'''NESTED IF'''

# 82). Write a program to print middle value of the given heterogeneous tuple collection only if the middle value is string and having the length greater than 3 
tpl = eval(input("Enter a Tuple: "))    
mid_index = len(tpl) // 2
middle_value = tpl[mid_index]

if type(middle_value) == str:
    if len(middle_value) > 3:
        print(middle_value)
    else:
        print("It is a string but the length is not greater than 3")
else:
    if type(middle_value) != str:
        print("the mid vale is not string")
        

#######################################################################
#######################################################################
