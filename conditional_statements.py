######################################################################
######################################################################
'''SIMPLE IF'''
11.Write a program To register.For a company only if job location is Bangalore.

job_location = input("Enter the job location:")
if job_location=="bangalore":
    name = input("Enter your name:")
    email = input("Enter your Email-ID:")
    phno = int(input("Enter your phone number:"))
    password = input("Enter your Password:")
    print("Registration Successful")


12.Write a program to check whether the given number is even 

num = int(input("Enter a number:"))
if num % 2 == 0:
    print(f"{num} is a even number")
    

13. Write a program to check whether the given number is odd 

num = int(input("Enter num:"))
if num % 2 != 0:
    print(f"The given number {num} is Odd")


14.Write a program to check whether the given number lies between 5 to 10 
 
num = int(input("Enter a number:"))
if 5 < num < 10:
    print(f"{num} lies between 5 to 10")
    
15.Write a program To check whether the given string is having more than three characters 

word = input("Enter word:")
if len(word) > 3:
    print(f"The {word} has more than three characters")

16.

17.Write a program to check whether the given character is a vowel 
 
char = input("Enter a character:")
if char in "aeiouAEIOU":
    print(f"{char} is a vowel")



#######################################################################
#######################################################################
'''IF ELSE'''








#######################################################################
#######################################################################
'''ELIF'''
54. Write a program to check the relation between two integer numbers

num_1= int(input("enter the num 1: "))
num_2= int(input("enter the num 2: "))

if num_1 == num_2:
    print('Both Numbers are equal')
elif num_1 > num_2:
    print("Number 1 is greater than Number 2")
else:
    print("Number 2 is greater")

55. Write a program to check whether a given character is uppercase or lowercase or number. If character is uppercase print uppercase, If character is lowercase print lowercase. If the character is a number, print the ascii number of it.

char = input("Entrer a char: ")
if char.isnumeric():
    print(ord(char))
elif char.isupper():
    print("Char is upper case")
elif char.islower():
    print("char is lower case")
else:
    print("char is nither upper case nor lowercase nor number")

56. Write a program to check whether a given character is a vowel or consonant. If a given character is a vowel, store the character inside the list. If a given character is consonant, display the ASCII value of that character.

character = input("enter a alphabet: ")
vovel= []
if character.lower() in ['a','i','o','u','e']:
    vovel.append(character)
elif character.lower() in "bcdfghjklmnpqrstvwxyz":
    print(ord(character))
else:
    print("It is not an alphabet")

57. Write a program to check whether a given character is uppercase. If it is uppercase, convert it to lowercase.Else PRINT LOWERCASE.

char= input("enter a alphabet: ")

if char.isupper():
    print(char.lower())
else:
    print("It LOWER CASE")

58. Write a program to checkWhether the entered character is a number. If it is a number, print the ASCII value of that number.

character = input("Enter a character: ")

if character.isdigit():
    ascii_value = ord(character)  
    print(f"The ASCII value of '{character}' is: {ascii_value}")
else:
    print(f"The character '{character}' is not a number.")


59. Write a program to check whether given character is uppercase, print its lowercase character or if given character is lowercase print its uppercase character or if given character is special character print the character after adding 8 to the ascii value of that particle special character

char = input("enter the char: ")
if char.isupper():
    print(char.lower())
elif char.islower():
    print(char.upper())
elif char.isnumeric():
    print("Invalid Input")
else:
    print(ord((char))+8)
    
    
60. Write a program to check whether the last character of a given string is a special character or not.

char = input("enter a string: ")
if char[-1].isalnum():
    print("It is not a special character")
else:
    print("It is a special character")

61. Write a program to check if the middle value of heterogeneous tuple collection is integer or not.

tpl= eval(input("enter a tupple: "))
mid_index= len(tpl) // 2
mid_value = tpl[mid_index]

if type(mid_value) == int:
    print("The middle value is Integer")
else:
    print("The middle value is not integer")

63. write a program to check whether the given integer single digit or two digits or three digits or more than three digits

num= int(input("enter a number: "))
if -9 <= num <= 9:
    print("It is a single digit")
elif -99 <= num <= 99:
    print("It is a two digit")
elif -999 <= num <= 999:
    print("It is three digit")
else:
    print("It is more than three digit")

65. Write a program to predict grade of the student based on the obtained result

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

66. Write a program to check whether the entered character is uppercase or lowercase or number or special character

char = input("enter the char: ")
if char.isupper():
    print("The character is uppercase")
elif char.islower():
    print("The character is lowercase")
elif char.isnumeric():
    print("The character is numeric")
else:
    print("The character is a special character")

67. Write a program to find the greatest among two numbers

num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

if num_1 > num_2:
    print(f"The greatest number is: {num_1}")
elif num_2 > num_1:
    print(f"The greatest number is: {num_2}")
else:
    print("Both numbers are equal.")


68. Write a program to find the smallest among three numbers

num_1 = float(input('enter a number'))
num_2 = float(input('enter a number'))
num_3 = float(input('enter a number'))

if num_1 <= num_2 and num_1 <= num_3:
    print(f"{num_1}")
elif num_2 <= num_1 and num_2 <= num_3:
    print(num_2)
else:
    print(num_3)

69. Write a program to find the greatest among four numbers

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

71. Write a program to calculate the electricity bill.According to the following criteria, for 1st 100 units there is no charge, For next 100 units there is ₹5 per unit and after 200 units, the price is rupees 10 per unit.If the input is 350 then total bill amount is Rupees 2000.

units= int(input("Enter the units: "))
Total_Bill= 0.0

if 0 <= units <= 100:
    Total_Bill = 0.0
elif 0<= units <= 200:
    Total_Bill = (units-100)*5
elif units > 200:
    Total_Bill = (units-200)*10 + (100*5)

print(f"The total bill for {units} units is Rs {Total_Bill}")

80. WAP to convert temperature from celsius to kelvin and kelvin to celsius using the elif statement.

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

82). Write a program to print middle value of the given heterogeneous tuple collection only if the middle value is string and having the length greater than 3 

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
